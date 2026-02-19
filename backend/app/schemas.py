from pydantic import BaseModel

class TranscriptIn(BaseModel):
    text: str

class SoapOut(BaseModel):
    soap: str
    disclaimer: str
    flags: list[str]