from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def get_pipeline():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )