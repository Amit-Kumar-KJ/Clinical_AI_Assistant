import os
from fastapi import FastAPI, HTTPException, Header
from .schemas import TranscriptIn, SoapOut
from .prompts import SYSTEM_INSTRUCTION, SOAP_FORMAT
from .guardrails import validate_transcript, basic_flags
from .gemini_client import generate_text

app = FastAPI(title="Clinical AI Assistant (MVP)")

DISCLAIMER = (
    "Disclaimer: This tool assists clinical documentation only and does not provide medical advice. "
    "A licensed clinician must review and edit the generated note before use."
)

APP_API_KEY = os.getenv("APP_API_KEY")

def require_key(x_api_key: str | None):
    if APP_API_KEY and x_api_key != APP_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate", response_model=SoapOut)
def generate(data: TranscriptIn,  x_api_key: str | None = Header(default=None)):
    require_key(x_api_key)
    try:
        transcript = validate_transcript(data.text)
        flags = basic_flags(transcript)

        prompt = (
            f"{SYSTEM_INSTRUCTION}\n\n"
            f"{SOAP_FORMAT}\n\n"
            f"Transcript:\n{transcript}\n"
        )

        soap = generate_text(prompt)
        if not soap:
            raise RuntimeError("Model returned empty output.")

        return SoapOut(soap=soap, disclaimer=DISCLAIMER, flags=flags)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation failed: {e}")
