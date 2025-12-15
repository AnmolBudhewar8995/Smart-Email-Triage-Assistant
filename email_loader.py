# src/email_loader.py
import email
from email import policy
from pathlib import Path

def load_eml_files(folder="data/emails"):
    emails = []
    for file in Path(folder).glob("*.eml"):
        with open(file, "rb") as f:
            msg = email.message_from_bytes(f.read(), policy=policy.default)

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_content()
        else:
            body = msg.get_content()

        emails.append({
            "subject": msg.get("subject", ""),
            "from": msg.get("from", ""),
            "date": msg.get("date", ""),
            "body": body.strip()
        })
    return emails
