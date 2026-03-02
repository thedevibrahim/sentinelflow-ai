from fastapi import FastAPI
from pydantic import BaseModel
from model import get_pipeline

app = FastAPI(title="SentinelFlow AI Model Service")

nlp = get_pipeline()

class TextInput(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(input: TextInput):
    result = nlp(input.text)[0]
    return {
        "label": result["label"],
        "score": float(result["score"])
    }