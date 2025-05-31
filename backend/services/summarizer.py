import os
import requests
from dotenv import load_dotenv
import json
import re

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def get_summary_from_gemini(content: str):
    prompt = f"""
        Analyze the following content and return a structured JSON object with keys:
        "summary", "important_points", and "anecdotes".

        Each key should contain relevant content based on the analysis of the input.
        Do NOT include any markdown, code fences, or explanations — only return valid JSON.

        Content:
        \"\"\"
        {content}
        \"\"\"

        Expected output format:
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

            # Extract content inside ```json ... ``` if present
            if "```json" in text:
                match = re.search(r"```json(.*?)```", text, re.DOTALL)
                if match:
                    text = match.group(1).strip()
            else:
                # Fallback: clean up extra whitespace
                text = text.strip()

            parsed = json.loads(text)
            return parsed

        except Exception as e:
            # Fall back gracefully if parsing fails
            return {
                "summary": text,
                "important_points": [],
                "anecdotes": [],
                "note": "Unstructured or unparseable response"
            }
    else:
        return {"error": response.text}