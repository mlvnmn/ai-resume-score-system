"""
Machine Learning Module
Computes semantic similarity between resume text and job description
using TF-IDF + cosine similarity (scikit-learn).
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(resume_text: str, job_description: str) -> float:
    """
    Calculate cosine similarity between resume and job description
    using TF-IDF vectorisation.
    Returns a score between 0.0 and 1.0.
    """
    if not resume_text.strip() or not job_description.strip():
        return 0.0

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000,
        ngram_range=(1, 2),
    )
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return float(similarity[0][0])


def compute_skill_match_percentages(
    resume_skills: list[str],
    required_skills: list[str],
) -> list[dict]:
    """
    For each required skill, calculate a match percentage.
    - 100% if the skill is present in the resume.
    -  0% if absent.
    Returns a list of {"name": str, "percentage": int}.
    """
    results = []
    resume_lower = {s.lower() for s in resume_skills}
    for skill in required_skills:
        matched = skill.lower() in resume_lower
        results.append({
            "name": skill,
            "percentage": 100 if matched else 0,
        })
    return results
