import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def get_summary_from_gemini(content: str):
    prompt = f"""
       Analyze the following content and return the result in JSON format with keys: 
        "summary", "important_points", and "anecdotes".

        Content:
        \"\"\"
        {content}
        \"\"\"

        Example output format:
        {{
        "summary": "Short summary here...",
        "important_points": [
            "Point 1",
            "Point 2"
        ],
        "anecdotes": [
            "Anecdote 1",
            "Anecdote 2"
        ]
        }}
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
        try:
            text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
             # Clean markdown-formatted JSON
            if text.strip().startswith("```json"):
                text = text.strip().removeprefix("```json").removesuffix("```").strip()

            parsed = json.loads(text)
            return parsed
        except Exception as e:
            return {"summary": text, "important_points": [], "anecdotes": [], "note": "Unstructured response"}
    else:
        return {"error": response.text}