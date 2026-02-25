#!/usr/bin/env bash
# build.sh — Render build command
# Builds the React frontend and installs Python backend dependencies.

set -o errexit  # exit on error

echo "=== Installing Node.js dependencies ==="
npm install

echo "=== Building React frontend ==="
npm run build

echo "=== Installing Python dependencies ==="
pip install -r backend/requirements.txt

echo "=== Downloading NLTK data ==="
python -c "
import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
print('NLTK data downloaded successfully')
"

echo "=== Build complete ==="
