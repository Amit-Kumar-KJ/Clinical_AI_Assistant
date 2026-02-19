import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY missing. Put it in backend/.env")

client = genai.Client(api_key=API_KEY)

def generate_text(prompt: str) -> str:
    resp = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    return (resp.text or "").strip()
