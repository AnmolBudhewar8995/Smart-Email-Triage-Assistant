# Smart Email Triage Assistant

An AI-powered email triage tool built with Streamlit that automatically classifies, prioritizes, summarizes, and suggests replies for your emails.

## Features

- **Email Classification**: Automatically categorizes emails into Work, Personal, Urgent, Spam, Newsletter, or Promotions using zero-shot classification.
- **Priority Assessment**: Determines email priority (High, Medium, Low) based on keywords in subject and body.
- **Email Summarization**: Generates concise summaries of email content using advanced NLP models.
- **Smart Reply Suggestions**: Provides context-aware reply suggestions based on email category and priority.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd smart-email-triage-assistant
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your `.eml` email files in the `data/emails/` directory.

2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

3. Open your browser to the provided URL (usually `http://localhost:8501`) to access the email triage interface.

## Project Structure

- `app.py`: Main Streamlit application
- `src/`: Source code modules
  - `email_loader.py`: Loads and parses EML files
  - `classifier.py`: Email classification using transformers
  - `priority.py`: Priority assessment logic
  - `summarizer.py`: Email summarization
  - `responder.py`: Reply suggestion logic
- `requirements.txt`: Python dependencies
- `data/emails/`: Directory for EML files (create this directory)

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

## Technologies Used

- Streamlit for the web interface
- Transformers (Hugging Face) for NLP tasks
- Python's built-in `email` module for parsing EML files
