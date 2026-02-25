"""
NLP Processing Module
Text preprocessing, keyword extraction, and skill identification using NLTK and spaCy.
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data (runs once)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

STOP_WORDS = set(stopwords.words("english"))

# ─── Curated skill/keyword dictionary ───────────────────────────────────────
KNOWN_SKILLS = {
    # Programming languages
    "python", "java", "javascript", "typescript", "c++", "c#", "go", "rust",
    "ruby", "php", "swift", "kotlin", "scala", "r", "matlab", "perl",
    # Web frameworks & libraries
    "react", "angular", "vue", "next.js", "nuxt", "svelte", "django",
    "flask", "fastapi", "express", "spring", "rails", "laravel",
    # Data / ML
    "tensorflow", "pytorch", "keras", "scikit-learn", "pandas", "numpy",
    "matplotlib", "seaborn", "opencv", "nltk", "spacy", "huggingface",
    "transformers", "llm", "gpt", "bert", "machine learning",
    "deep learning", "natural language processing", "nlp",
    "computer vision", "data science", "data analysis", "data engineering",
    "statistics", "big data",
    # Databases
    "sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch",
    "dynamodb", "cassandra", "sqlite", "firebase",
    # Cloud & DevOps
    "aws", "azure", "gcp", "google cloud", "docker", "kubernetes",
    "terraform", "ansible", "jenkins", "ci/cd", "github actions",
    "linux", "nginx", "apache",
    # Tools & concepts
    "git", "github", "gitlab", "jira", "agile", "scrum",
    "rest", "graphql", "api", "microservices", "serverless",
    "html", "css", "sass", "tailwind", "bootstrap",
    "figma", "photoshop", "ui/ux",
    # Soft skills (weighted lower but still extracted)
    "leadership", "communication", "teamwork", "problem solving",
    "project management", "analytical", "critical thinking",
}


def clean_text(text: str) -> str:
    """Lowercase, strip extra whitespace, remove special characters."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\+\#\./]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_and_filter(text: str) -> list[str]:
    """Tokenize and remove stop words."""
    tokens = word_tokenize(text)
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 1]


def extract_keywords(text: str) -> list[str]:
    """
    Extract meaningful keywords from resume text.
    Returns a deduplicated, sorted list of keywords.
    """
    cleaned = clean_text(text)
    tokens = tokenize_and_filter(cleaned)

    # Bigrams for multi-word skills like "machine learning"
    bigrams = [f"{tokens[i]} {tokens[i+1]}" for i in range(len(tokens) - 1)]
    trigrams = [
        f"{tokens[i]} {tokens[i+1]} {tokens[i+2]}" for i in range(len(tokens) - 2)
    ]

    candidates = set(tokens) | set(bigrams) | set(trigrams)
    extracted = sorted({s for s in candidates if s in KNOWN_SKILLS})
    return extracted


def extract_skills_from_text(text: str) -> list[str]:
    """
    Directly match known skills in the raw text (case-insensitive).
    More reliable than pure tokenization for compound terms.
    """
    lower_text = clean_text(text)
    found = []
    for skill in sorted(KNOWN_SKILLS, key=len, reverse=True):
        if skill in lower_text:
            found.append(skill)
    return sorted(set(found))
