"""
FastAPI Application — AI Resume Screening & ATS Score System
Serves the React frontend (static) and exposes API endpoints.
"""

import os
import sys

# Ensure the backend directory is on the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from modules.resume_parser import parse_resume
from modules.nlp_processor import extract_skills_from_text
from modules.ats_scorer import calculate_ats_score
from modules.recommender import generate_recommendations
from modules.job_descriptions import get_job_description, list_available_roles

# ─── App setup ───────────────────────────────────────────────────────────────
app = FastAPI(
    title="ResumeAI Backend",
    description="AI-Based Resume Screening and ATS Score System",
    version="1.0.0",
)

# CORS — allow dev and production origins
allowed_origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3000",
]

# In production on Render, also allow the Render URL
RENDER_EXTERNAL_URL = os.environ.get("RENDER_EXTERNAL_URL")
if RENDER_EXTERNAL_URL:
    allowed_origins.append(RENDER_EXTERNAL_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Response models ─────────────────────────────────────────────────────────
class SkillMatch(BaseModel):
    name: str
    percentage: int


class AnalysisResponse(BaseModel):
    fileName: str
    atsScore: int
    skills: list[SkillMatch]
    missingKeywords: list[str]
    recommendations: list[str]


class BatchAnalysisResponse(BaseModel):
    results: list[AnalysisResponse]
    failed: list[str]


class RoleItem(BaseModel):
    key: str
    title: str
    category: str


# ─── API Endpoints ───────────────────────────────────────────────────────────

@app.get("/api/roles", response_model=list[RoleItem])
async def get_roles():
    """List all available job roles for the dropdown."""
    return list_available_roles()


@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze_resume(
    file: UploadFile = File(...),
    role: str = Form(default="software_engineer"),
):
    """
    Upload a resume and receive an ATS analysis.
    - file:  PDF or DOCX resume
    - role:  job role key (default: software_engineer)
    """
    # Validate file type
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided.")

    allowed = (".pdf", ".docx", ".doc")
    if not file.filename.lower().endswith(allowed):
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported format. Please upload {', '.join(allowed)}.",
        )

    # Validate file size (max 5 MB)
    contents = await file.read()
    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File exceeds 5 MB limit.")

    # Get job description
    job = get_job_description(role)
    if not job:
        raise HTTPException(status_code=400, detail=f"Unknown role: {role}")

    # 1 — Parse resume
    try:
        resume_text = parse_resume(contents, file.filename)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not resume_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from the file. The PDF may be image-based.",
        )

    # 2 — ATS scoring
    result = calculate_ats_score(
        resume_text=resume_text,
        job_description=job["description"],
        required_skills=job["required_skills"],
    )

    # 3 — Recommendations
    recommendations = generate_recommendations(
        missing_skills=result["missingKeywords"],
        similarity_score=result["similarityScore"],
        formatting_score=result["formattingScore"],
        keyword_coverage=result["keywordCoverage"],
        resume_text=resume_text,
    )

    return AnalysisResponse(
        fileName=file.filename,
        atsScore=result["atsScore"],
        skills=result["skills"],
        missingKeywords=result["missingKeywords"],
        recommendations=recommendations,
    )


@app.post("/api/analyze-batch", response_model=BatchAnalysisResponse)
async def analyze_batch_resumes(
    files: list[UploadFile] = File(...),
    role: str = Form(default="software_engineer"),
):
    """
    Upload multiple resumes and receive ranked ATS analyses.
    - files: list of PDF or DOCX resumes
    - role:  job role key (default: software_engineer)
    """
    if not files:
        raise HTTPException(status_code=400, detail="No files provided.")

    # Get job description
    job = get_job_description(role)
    if not job:
        raise HTTPException(status_code=400, detail=f"Unknown role: {role}")

    allowed = (".pdf", ".docx", ".doc")
    results = []
    failed = []

    for file in files:
        if not file.filename:
            continue
            
        if not file.filename.lower().endswith(allowed):
            failed.append(f"{file.filename} (Unsupported format)")
            continue

        contents = await file.read()
        if len(contents) > 5 * 1024 * 1024:
            failed.append(f"{file.filename} (Exceeds 5MB limit)")
            continue

        try:
            resume_text = parse_resume(contents, file.filename)
            if not resume_text.strip():
                failed.append(f"{file.filename} (Empty or image-based)")
                continue

            result = calculate_ats_score(
                resume_text=resume_text,
                job_description=job["description"],
                required_skills=job["required_skills"],
            )

            recommendations = generate_recommendations(
                missing_skills=result["missingKeywords"],
                similarity_score=result["similarityScore"],
                formatting_score=result["formattingScore"],
                keyword_coverage=result["keywordCoverage"],
                resume_text=resume_text,
            )

            results.append(AnalysisResponse(
                fileName=file.filename,
                atsScore=result["atsScore"],
                skills=result["skills"],
                missingKeywords=result["missingKeywords"],
                recommendations=recommendations,
            ))
        except Exception as e:
            failed.append(f"{file.filename} (Error: {str(e)})")

    # Sort results by ATS score descending
    results.sort(key=lambda x: x.atsScore, reverse=True)

    return BatchAnalysisResponse(
        results=results,
        failed=failed
    )

# ─── Health check ────────────────────────────────────────────────────────────

@app.get("/api/health")
async def health():
    return {"status": "healthy"}


# ─── Serve React Static Frontend ─────────────────────────────────────────────
# The built React app is placed in ../dist by the Render build script.
# We mount it LAST so API routes take priority.

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dist")

if os.path.isdir(STATIC_DIR):
    # Serve static assets (JS, CSS, images)
    app.mount("/assets", StaticFiles(directory=os.path.join(STATIC_DIR, "assets")), name="assets")

    # Catch-all: serve index.html for any non-API route (SPA routing)
    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        # If a specific file exists in dist, serve it
        file_path = os.path.join(STATIC_DIR, full_path)
        if full_path and os.path.isfile(file_path):
            return FileResponse(file_path)
        # Otherwise serve index.html (SPA client-side routing)
        return FileResponse(os.path.join(STATIC_DIR, "index.html"))
