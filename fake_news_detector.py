from google import genai
from dotenv import load_dotenv
import os


# --------------------------------
# Load Environment Variables
# --------------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found in .env file")
    exit()

client = genai.Client(api_key=api_key)


# --------------------------------
# Banner
# --------------------------------
def banner():

    print("=" * 60)
    print("🔍 AI Fake News Detector")
    print("🚀 Made by cr1ms0ncode")
    print("=" * 60)
    print()


# --------------------------------
# User Input
# --------------------------------
def get_news():

    print("Paste any news headline, message, article, or claim.")
    print()

    news = input("News Content:\n> ")

    return news


# --------------------------------
# Build Prompt
# --------------------------------
def build_prompt(news):

    return f"""
You are an expert fact-checking assistant.

Analyze the following claim carefully.

CLAIM:
{news}

Rules:

Do NOT assume the claim is true.

If evidence is insufficient, say UNVERIFIED.

Provide response in this format:

VERDICT:
(LIKELY TRUE / LIKELY FALSE / MISLEADING / UNVERIFIED)

CONFIDENCE:
(0-100%)

WHY THIS VERDICT:
(3 detailed reasons)

RED FLAGS:
(List suspicious signs if any)

WHAT TO VERIFY:
(What sources should be checked)

USER ADVICE:
(What the user should do next)

Answer in simple Hinglish.
"""


# --------------------------------
# Generate Analysis
# --------------------------------
def analyze_news(prompt):

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"❌ Error: {e}"


# --------------------------------
# Save Report
# --------------------------------
def save_report(report):

    with open(
        "fact_check_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print()
    print("✅ Report Saved")
    print("📄 File: fact_check_report.txt")


# --------------------------------
# Main Program
# --------------------------------
def main():

    banner()

    news = get_news()

    print()
    print("🔍 Analyzing News...")
    print()

    prompt = build_prompt(news)

    report = analyze_news(prompt)

    print("=" * 60)
    print(report)
    print("=" * 60)

    save_report(report)


# --------------------------------
# Run App
# --------------------------------
if __name__ == "__main__":
    main()