import time
import requests
from pathlib import Path
import os 
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]   # metrics/ -> root/
ENV_PATH = BASE_DIR / "backend" / ".env"

load_dotenv(ENV_PATH)

API_KEY = os.getenv("APP_API_KEY")
if not API_KEY:
    raise RuntimeError("APP_API_KEY not found. Set it in your environment.")

URL = "https://clinical-ai-assistant-61ui.onrender.com/generate"
HEADERS = {"Content-Type": "application/json", "X-API-KEY": API_KEY}

PAYLOAD = {
    "text": (
        "Doctor: What brings you in today? Patient: I have had fever and cough for 3 days. "
        "Doctor: Any breathlessness? Patient: No. Doctor: Took paracetamol."
    )
}

DURATION_SECONDS = 60
count = 0
start = time.perf_counter()

while True:
    now = time.perf_counter()
    if now - start >= DURATION_SECONDS:
        break
    r = requests.post(URL, headers=HEADERS, json=PAYLOAD, timeout=120)
    if r.status_code == 200:
        count += 1

elapsed = time.perf_counter() - start
print(f"Successful requests: {count} in {elapsed:.1f}s")
print(f"Throughput: {count / (elapsed/60):.1f} requests/min")
