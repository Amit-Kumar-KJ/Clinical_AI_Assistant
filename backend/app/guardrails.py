MIN_CHARS = 80

def validate_transcript(text: str) -> str:
    text = (text or "").strip()
    if len(text) < MIN_CHARS:
        raise ValueError("Transcript too short. Please paste a fuller conversation.")
    return text

def basic_flags(text: str) -> list[str]:
    flags = []
    low = text.lower()
    if "ignore previous" in low or "system prompt" in low:
        flags.append("Possible prompt-injection content detected.")
    return flags
