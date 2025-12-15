# src/classifier.py
from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

LABELS = [
    "Work",
    "Personal",
    "Urgent",
    "Spam",
    "Newsletter",
    "Promotions"
]

def classify_email(text):
    result = classifier(text, LABELS)
    return result["labels"][0], round(result["scores"][0], 3)
