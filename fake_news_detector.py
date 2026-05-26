from google import genai

print("=" * 55)
print("   AI Fake News Detector 🔍")
print("   Made by cr1ms0ncode 🚀")
print("=" * 55)
print()
print("SETUP: aistudio.google.com se API key lo")
print()

api_key = input("Enter your Gemini API Key: ")
client = genai.Client(api_key=api_key)

print()
news = input("Koi bhi news headline ya content paste karo:\n> ")

print()
print("Analyzing... 🔍")
print()

prompt = f"""
Tum ek expert fact-checker ho. Neeche di gayi news ko analyze karo:

NEWS: {news}

Analysis do in this format:
VERDICT: (REAL / FAKE / MISLEADING / UNVERIFIED)
CONFIDENCE: (percentage)
REASONS: (3 solid reasons for your verdict)
RED FLAGS: (suspicious elements if any)
ADVICE: (user ko kya karna chahiye)

Hinglish mein jawab do.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

print("=" * 55)
print(response.text)
print("=" * 55)