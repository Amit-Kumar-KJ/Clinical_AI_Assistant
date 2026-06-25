from pydantic import BaseModel

class Subjective(BaseModel):
    chief_complaint: str
    hpi: str
    pmh: str
    medications: str
    allergies: str
    social_history: str
    ros: str

class Objective(BaseModel):
    vitals: str
    physical_exam: str
    labs_imaging: str

class Assessment(BaseModel):
    problem_list: str

class Plan(BaseModel):
    diagnostics: str
    treatment: str
    patient_education: str
    follow_up: str

class SoapNote(BaseModel):
    subjective: Subjective
    objective: Objective
    assessment: Assessment
    plan: Plan

class TranscriptIn(BaseModel):
    text: str

class SoapOut(BaseModel):
    soap: SoapNote
    disclaimer: str
    flags: list[str]