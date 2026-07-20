from pydantic import BaseModel
from fastapi import FastAPI
from analyzer import PasswordAnalyzer

app = FastAPI()

class PasswordRequest(BaseModel):
    password: str

@app.get("/")
def home():
    return {"message": "Welcome to my Password Checker API!"}

@app.post("/check")
def check_password(request: PasswordRequest):
    analyzer = PasswordAnalyzer(request.password)

    score, feedback = analyzer.score_password()
    strength = analyzer.classify_strength(score)

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }
