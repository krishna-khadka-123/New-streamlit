from google import genai

# Paste your Gemini API key here temporarily
API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"

client = genai.Client(api_key=API_KEY)

def generate_content(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text
    )
    return response.text