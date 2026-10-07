"""AI-assisted analysis of a user-provided news claim."""

import os
import sys

from dotenv import load_dotenv
from google import genai


MODEL = "gemini-2.0-flash"


def build_prompt(news: str) -> str:
    return f"""You are an assistant analyzing a user-provided claim, not a source-verification system.

CLAIM:
{news}

Do not assume the claim is true. Clearly say when evidence is insufficient. Do not invent sources,
citations, or verification. Give a tentative verdict, explain uncertainty, list what primary sources
should be checked, and give practical advice. Answer in simple Hinglish.
"""


def analyze_news(news: str, client) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=build_prompt(news),
    )
    result = response.text
    if not result or not result.strip():
        raise RuntimeError("The model returned an empty response.")
    return result.strip()


def save_report(report: str, path: str = "fact_check_report.txt") -> None:
    with open(path, "w", encoding="utf-8") as report_file:
        report_file.write(report + "\n")


def main() -> int:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or api_key == "your_api_key_here":
        print("GEMINI_API_KEY is missing. Copy .env.example to .env and add your key.", file=sys.stderr)
        return 1

    news = input("Paste a news headline, message, article, or claim:\n> ").strip()
    if not news:
        print("Please enter a claim to analyze.", file=sys.stderr)
        return 1

    try:
        report = analyze_news(news, genai.Client(api_key=api_key))
    except Exception as error:
        print(f"Analysis failed: {error}", file=sys.stderr)
        return 1

    print("\n" + "=" * 60 + "\n" + report + "\n" + "=" * 60)
    save_report(report)
    print("Report saved to fact_check_report.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
