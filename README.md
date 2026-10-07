# AI Fake News Detector

A small command-line demo that uses Google Gemini to analyze a claim and suggest what a reader should verify.

## What it does

- Accepts a headline, article excerpt, or claim.
- Produces a tentative AI-generated analysis in Hinglish.
- Saves the result to `fact_check_report.txt`.

This project does **not** independently verify claims or retrieve evidence. Model output can be inaccurate; check original reporting, official records, and other reliable sources before relying on it.

## Setup

Requires Python 3.10 or newer.

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set `GEMINI_API_KEY` to a key from [Google AI Studio](https://aistudio.google.com/). Keep `.env` private; it is ignored by Git.

Run the program:

```sh
python fake_news_detector.py
```

## Security

If an API key was ever committed or shared, revoke it and create a replacement. Removing a key in a new commit does not remove it from Git history.
