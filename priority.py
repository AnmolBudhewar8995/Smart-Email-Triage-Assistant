# src/priority.py
URGENT_KEYWORDS = [
    "urgent", "asap", "immediately", "deadline",
    "important", "action required", "today"
]

def compute_priority(subject, body):
    text = (subject + " " + body).lower()
    score = 0

    for kw in URGENT_KEYWORDS:
        if kw in text:
            score += 1

    if score >= 2:
        return "High"
    elif score == 1:
        return "Medium"
    else:
        return "Low"
