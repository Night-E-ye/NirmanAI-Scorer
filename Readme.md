## 🚀 Nirmaan AI – Transcript Scoring System
AI-powered Self-Introduction Rubric Evaluator
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" /> <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi" /> <img src="https://img.shields.io/badge/NLP-SentenceTransformers-orange" /> <img src="https://img.shields.io/badge/Frontend-HTML/JS-yellow" /> </p>
# Nirmaan AI - Rubric Scorer

## Overview
A small app that scores short self-introduction transcripts using a rule + NLP + rubric-driven hybrid.

## Run locally
    1. python -m venv venv
    2. source venv/bin/activate
    3. pip install -r requirements.txt
    4. uvicorn main:app --reload
    5. open index.html and paste transcript, click Score

## Files
- main.py: FastAPI server and example rubric
- scorer.py: core scoring logic using sentence-transformers
- index.html: minimal UI

## How scoring works
Per-criterion scores computed as weighted combination of:
- rule-based keyword match
- semantic similarity (sentence-transformers)
- grammar estimate
Rubric weights are respected as provided in the input Excel.

## Screenshots

<img width="1874" height="510" alt="Screenshot 2025-11-23 225407" src="https://github.com/user-attachments/assets/cab40467-c47b-473e-8d6d-7b21f001fd7b" />
<img width="742" height="664" alt="Screenshot 2025-11-23 225606" src="https://github.com/user-attachments/assets/9e78008f-8498-4fb3-b6af-cc32febe2061" />
<img width="1753" height="275" alt="image" src="https://github.com/user-attachments/assets/938ef934-9945-4c66-a3c0-10b601bdcf73" />






