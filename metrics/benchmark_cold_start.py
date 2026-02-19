import time
import requests
import os
from dotenv import load_dotenv
load_dotenv("backend/.env")
URL = "https://clinical-ai-assistant-61ui.onrender.com/generate"

API_KEY = os.getenv("APP_API_KEY")
if not API_KEY:
    raise RuntimeError("APP_API_KEY not found. Set it in your environment.")

HEADERS = {"Content-Type": "application/json", "X-API-KEY": API_KEY}
PAYLOAD = {"text": "Doctor: Patient reports fever and cough for 3 days. No chest pain. Took paracetamol twice."}

start = time.perf_counter()
r = requests.post(URL, headers=HEADERS, json=PAYLOAD, timeout=180)
elapsed = time.perf_counter() - start

print("Status:", r.status_code)
print(f"Cold-start request time: {elapsed:.3f}s")
