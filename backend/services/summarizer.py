import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def get_summary_from_gemini(content: str):
    prompt = f"""
        Summarize this content:

        {content}

        Please provide:
        1. A short summary
        2. Important points
        3. Any anecdotes mentioned
    """

    """
        EXPECTED PAYLOAD:
        curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY" \
        -H 'Content-Type: application/json' \
        -X POST \
        -d '{
            "contents": [
            {
                "parts": [
                {
                    "text": "Explain how AI works in a few words"
                }
                ]
            }
            ]
        }'
    """
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 512
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(GEMINI_URL, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Extract the generated text from the API response
        summary_text = data["candidates"][0]["content"]["parts"][0]["text"]
        return summary_text
    else:
        return f"Error from Gemini API: {response.text}"