🚀 Nirmaan AI – Transcript Scoring System
AI-powered Self-Introduction Rubric Evaluator
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" /> <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi" /> <img src="https://img.shields.io/badge/NLP-SentenceTransformers-orange" /> <img src="https://img.shields.io/badge/Frontend-HTML/JS-yellow" /> </p>
📌 Overview

This project evaluates self-introduction transcripts using:

🔹 Rule-based scoring

🔹 NLP semantic similarity (Sentence-BERT)

🔹 Keyword matching

🔹 Grammar estimation

🔹 Sentiment scoring

🔹 Rubric weightage from Excel

It returns:

✔ Overall score (0–100)
✔ Per-criterion breakdown
✔ Word count
✔ Keyword hits
✔ Semantic similarity

Everything is dynamic and driven from an Excel rubric.

🖼️ Screenshot Preview

(Add your screenshots later)

[ Upload score UI screenshot here ]

📂 Project Structure
Nirmaan-AI/
│── main.py                 # FastAPI backend
│── scorer.py               # NLP + rule-based scoring logic
│── index.html              # Frontend client
│── requirements.txt
│
│── data/
│     ├── rubric.xlsx       # Real rubric (input)
│     └── rubric.json       # Auto-generated normalized rubric
│
│── scripts/
│     └── load_rubric.py    # Excel → JSON rubric converter
│
└── README.md

⚙️ Features
🧠 NLP-Powered Scoring

Sentence-BERT embeddings

VADER sentiment

Filler-word clarity scoring

Grammar check (light heuristic)

📊 Excel-Based Rubric

Supports flexible columns:

weight

must_keywords

good_keywords

min_words / max_words
…and more.

🔥 FastAPI Backend

/score → analyze transcript

/health → server check

🖥️ Frontend UI

Simple HTML interface for testing.

🛠️ Run Locally
1️⃣ Create Virtual Environment
python -m venv venv

2️⃣ Activate
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt
pip install pandas openpyxl

📊 Load Your REAL Rubric

Place your rubric at:

data/rubric.xlsx


Run:

python scripts/load_rubric.py


Generates:

data/rubric.json

🚀 Start the API Server
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

🌐 Use Frontend
✔ Option A — open directly

Double-click index.html

✔ Option B (recommended)
python -m http.server 8001


Open:

http://127.0.0.1:8001/index.html

📥 Sample API Request
{
  "transcript": "Hello everyone, my name is Muskan..."
}

📤 Sample Response
{
  "overall_score": 64.01,
  "words": 134,
  "per_criteria": [...],
  "debug": { "similarity": 0.63 }
}

📘 Architecture Diagram

(Add if you want)

Transcript → Preprocessing → Keyword Scoring
           → Embeddings → Semantic Similarity
           → Sentiment → Weighted Scoring → Final Score

☁ Deployment (Render / Railway)

Start command:

uvicorn main:app --host 0.0.0.0 --port 10000


Upload:

main.py

scorer.py

requirements.txt

data/rubric.xlsx

👤 Author

Built as part of Nirmaan AI Internship Assignment
By: Durgesh (Night-E-ye)
