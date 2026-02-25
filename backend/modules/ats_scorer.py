"""
ATS Scoring Engine
Combines similarity, keyword coverage, and formatting heuristics
into a single 0–100 ATS score.
"""

from modules.nlp_processor import extract_skills_from_text, extract_keywords
from modules.ml_model import compute_similarity, compute_skill_match_percentages


# ─── Scoring weights ────────────────────────────────────────────────────────
WEIGHT_SIMILARITY = 0.40   # TF-IDF cosine similarity
WEIGHT_SKILL_MATCH = 0.35  # % of required skills found
WEIGHT_KEYWORD_COV = 0.15  # keyword coverage breadth
WEIGHT_FORMATTING = 0.10   # basic formatting heuristics


def _check_formatting(text: str) -> float:
    """
    Simple heuristic score (0–1) for resume formatting quality.
    Checks for section headers, bullet points, and reasonable length.
    """
    score = 0.0
    lower = text.lower()

    # Has recognisable section headers?
    section_keywords = [
        "experience", "education", "skills", "projects",
        "summary", "objective", "certifications", "achievements",
    ]
    headers_found = sum(1 for kw in section_keywords if kw in lower)
    score += min(headers_found / 4, 1.0) * 0.4  # up to 0.4

    # Has bullet points or list markers?
    bullet_chars = ["•", "-", "●", "▪", "∗", "*"]
    has_bullets = any(c in text for c in bullet_chars)
    score += 0.2 if has_bullets else 0.0

    # Reasonable length (300–5000 words)?
    word_count = len(text.split())
    if 300 <= word_count <= 5000:
        score += 0.2
    elif 150 <= word_count < 300 or 5000 < word_count <= 8000:
        score += 0.1

    # Has contact info patterns (email, phone)?
    import re
    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text):
        score += 0.1
    if re.search(r"(\+?\d[\d\s\-]{7,})", text):
        score += 0.1

    return min(score, 1.0)


def calculate_ats_score(
    resume_text: str,
    job_description: str,
    required_skills: list[str],
) -> dict:
    """
    Master scoring function.
    Returns a dict with atsScore, skills, missingKeywords, recommendations.
    """
    # 1 — Semantic similarity
    similarity = compute_similarity(resume_text, job_description)

    # 2 — Skill matching
    resume_skills = extract_skills_from_text(resume_text)
    skill_matches = compute_skill_match_percentages(resume_skills, required_skills)
    matched_count = sum(1 for s in skill_matches if s["percentage"] > 0)
    skill_ratio = matched_count / len(required_skills) if required_skills else 0.0

    # 3 — Keyword coverage
    resume_keywords = set(extract_keywords(resume_text))
    jd_keywords = set(extract_keywords(job_description))
    if jd_keywords:
        keyword_overlap = len(resume_keywords & jd_keywords) / len(jd_keywords)
    else:
        keyword_overlap = 0.0

    # 4 — Formatting
    formatting_score = _check_formatting(resume_text)

    # ─── Weighted composite ──────────────────────────────────────────────
    raw_score = (
        WEIGHT_SIMILARITY * similarity
        + WEIGHT_SKILL_MATCH * skill_ratio
        + WEIGHT_KEYWORD_COV * keyword_overlap
        + WEIGHT_FORMATTING * formatting_score
    )
    ats_score = int(round(raw_score * 100))
    ats_score = max(0, min(100, ats_score))

    # 5 — Missing keywords
    missing_skills = [s["name"] for s in skill_matches if s["percentage"] == 0]

    return {
        "atsScore": ats_score,
        "skills": skill_matches,
        "missingKeywords": missing_skills,
        "similarityScore": round(similarity, 3),
        "skillMatchRatio": round(skill_ratio, 3),
        "keywordCoverage": round(keyword_overlap, 3),
        "formattingScore": round(formatting_score, 3),
    }
