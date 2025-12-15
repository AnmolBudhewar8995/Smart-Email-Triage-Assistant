# app.py
import streamlit as st
from src.email_loader import load_eml_files
from src.classifier import classify_email
from src.priority import compute_priority
from src.summarizer import summarize_email
from src.responder import suggest_reply

st.set_page_config(layout="wide")
st.title("📧 Smart Email Triage Assistant")

emails = load_eml_files()

if not emails:
    st.warning("No emails found. Add .eml files to data/emails/")
    st.stop()

for i, mail in enumerate(emails):
    with st.expander(f"📩 {mail['subject']}"):
        category, confidence = classify_email(mail["body"])
        priority = compute_priority(mail["subject"], mail["body"])
        summary = summarize_email(mail["body"])
        reply = suggest_reply(category, priority)

        st.markdown(f"**From:** {mail['from']}")
        st.markdown(f"**Category:** {category} ({confidence})")
        st.markdown(f"**Priority:** {priority}")
        st.markdown("### ✨ Summary")
        st.write(summary)
        st.markdown("### 💬 Suggested Reply")
        st.code(reply)
