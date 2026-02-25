"""
Recommendation Module
Generates actionable improvement suggestions based on the ATS analysis.
"""


def generate_recommendations(
    missing_skills: list[str],
    similarity_score: float,
    formatting_score: float,
    keyword_coverage: float,
    resume_text: str,
) -> list[str]:
    """
    Produce a list of human-readable improvement recommendations.
    """
    tips: list[str] = []

    # ─── Missing skills ─────────────────────────────────────────────────
    if missing_skills:
        top = missing_skills[:5]
        tips.append(
            f"Add these in-demand skills to your resume: {', '.join(top)}."
        )

    if len(missing_skills) > 5:
        tips.append(
            f"You are missing {len(missing_skills)} required skills — "
            "consider acquiring certifications or project experience in these areas."
        )

    # ─── Similarity / keyword match ──────────────────────────────────────
    if similarity_score < 0.3:
        tips.append(
            "Your resume has low semantic alignment with the job description. "
            "Rewrite your summary and experience sections to mirror the language "
            "used in the job posting."
        )
    elif similarity_score < 0.5:
        tips.append(
            "Improve keyword alignment by incorporating more terms from the "
            "job description into your work experience bullet points."
        )

    if keyword_coverage < 0.3:
        tips.append(
            "Many keywords from the job description are absent. Use the exact "
            "phrasing from the posting (e.g., \"cross-functional collaboration\" "
            "instead of \"teamwork\")."
        )

    # ─── Formatting ──────────────────────────────────────────────────────
    if formatting_score < 0.4:
        tips.append(
            "Improve your resume structure: add clear section headers "
            "(Experience, Education, Skills), use bullet points, and include "
            "your contact information."
        )

    lower = resume_text.lower()
    if "summary" not in lower and "objective" not in lower:
        tips.append(
            "Add a Professional Summary at the top of your resume tailored "
            "to the target role."
        )

    # ─── Quantification ─────────────────────────────────────────────────
    import re
    numbers = re.findall(r"\d+%|\d+\s*(?:users|clients|projects|revenue|sales)", lower)
    if len(numbers) < 2:
        tips.append(
            "Add quantifiable achievements — e.g., \"Increased API throughput "
            "by 40%\" or \"Managed a team of 8 engineers\"."
        )

    # ─── Generic best practices ──────────────────────────────────────────
    word_count = len(resume_text.split())
    if word_count < 200:
        tips.append(
            "Your resume is too short. Aim for at least 400–600 words to "
            "provide sufficient detail."
        )
    elif word_count > 5000:
        tips.append(
            "Your resume is very long. Consider condensing it to 1–2 pages "
            "for better ATS readability."
        )

    if not tips:
        tips.append(
            "Your resume is well-optimized! Consider tailoring it further "
            "for each specific application."
        )

    return tips
