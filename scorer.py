# scorer.py
import re
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download('punkt')

model = SentenceTransformer("all-MiniLM-L6-v2")
sentiment = SentimentIntensityAnalyzer()

def get_embedding(text):
    return model.encode([text])[0]

def score_transcript(transcript, rubric):
    words = len(re.findall(r'\w+', transcript))
    emb_text = get_embedding(transcript)

    results = []

    for crit in rubric:
        desc_emb = get_embedding(crit["description"])
        sim = cosine_similarity([emb_text], [desc_emb])[0][0]
        sim = float((sim+1)/2)

        must = crit["must"]
        found = 0
        for m in must:
            if m.lower() in transcript.lower():
                found += 1
        keyword_score = found / len(must) if must else 1

        raw = (0.6 * keyword_score + 0.4 * sim) * 100
        weighted = raw * (crit["weight"]/100)

        results.append({
            "id": crit["id"],
            "name": crit["name"],
            "score_raw": round(raw,2),
            "score_weighted": round(weighted,2),
            "similarity": round(sim,3)
        })

    overall = round(sum(r["score_weighted"] for r in results),2)

    return {
        "overall_score": overall,
        "words": words,
        "per_criteria": results
    }
