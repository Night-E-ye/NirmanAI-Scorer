# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from scorer import score_transcript

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Req(BaseModel):
    transcript: str

RUBRIC = [
    {"id":"salutation", "name":"Salutation", "description":"Greeting message", "must":["hello","hi"], "weight":5},
    {"id":"keywords","name":"Keyword Presence","description":"Personal details","must":["name","age","school","class","hobby"],"weight":30},
    {"id":"flow","name":"Flow","description":"Intro flow","must":["thank"],"weight":5},
    {"id":"grammar","name":"Grammar","description":"Language quality","must":[],"weight":10},
    {"id":"vocab","name":"Vocabulary","description":"Word richness","must":[],"weight":10},
    {"id":"clarity","name":"Clarity","description":"Clear speech","must":[],"weight":15},
    {"id":"engagement","name":"Engagement","description":"Positive tone","must":[],"weight":15}
]

@app.get("/")
def root():
    return {"msg":"Backend running"}

@app.post("/score")
def score(req: Req):
    return score_transcript(req.transcript, RUBRIC)
