# AI-Assisted Claim Review

A small Python CLI that asks Google Gemini to review a claim and return a structured response in simple Hinglish.

## What it does

- Requests a likely assessment and explanation
- Prompts for red flags and suggestions for what to verify
- Prints the response and saves it to `fact_check_report.txt`

This tool does not search for evidence, check sources, or verify claims. Treat the model's verdict and confidence as an unverified suggestion, not a fact-check. The output file is overwritten each time you run the program.

## Requirements

- Python 3
- A Google Gemini API key

## Setup

1. Clone the repository and enter its directory.
2. Create and activate a virtual environment:

   Windows PowerShell:

   ```powershell
   python -m venv .venv
   ./.venv/Scripts/Activate.ps1
   ```

   macOS/Linux:

   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```sh
   python -m pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and replace the placeholder with your key. In PowerShell, run `Copy-Item .env.example .env`; on macOS/Linux, run `cp .env.example .env`.
5. Run the CLI:

   ```sh
   python fake_news_detector.py
   ```

The text you enter is sent to Google's Gemini API. Keep your API key private and do not commit your populated `.env` file.

## Tech stack

- Python
- Google Gemini API via `google-genai`
- `python-dotenv` for local configuration

## Author

cr1ms0ncode
