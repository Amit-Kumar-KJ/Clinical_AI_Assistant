import time
import statistics
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
HEADERS = {
    "Content-Type": "application/json",
    "X-API-KEY": API_KEY
}

# Use a consistent transcript across runs (important!)
PAYLOAD = {
    "text": (
        "Doctor: What brings you in today? Patient: I have had fever and cough for 3 days. "
        "Doctor: Any breathlessness or chest pain? Patient: No chest pain, mild sore throat. "
        "Doctor: Any medications? Patient: Took paracetamol twice. "
        "Doctor: Any allergies? Patient: Not sure. "
        "Doctor: Okay, we’ll check temperature and recommend rest and fluids."
    )
}

RUNS = 20          # increase to 50 later for stronger confidence
TIMEOUT = 120      # LLM calls can take time

def percentile(values, p):
    """Return the pth percentile (0-100) using a simple sorted index method."""
    if not values:
        return None
    values_sorted = sorted(values)
    k = (len(values_sorted) - 1) * (p / 100)
    f = int(k)
    c = min(f + 1, len(values_sorted) - 1)
    if f == c:
        return values_sorted[f]
    return values_sorted[f] + (values_sorted[c] - values_sorted[f]) * (k - f)

times = []
status_counts = {}

print(f"Target: {URL}")
print(f"Runs: {RUNS}\n")

for i in range(RUNS):
    start = time.perf_counter()
    try:
        r = requests.post(URL, headers=HEADERS, json=PAYLOAD, timeout=TIMEOUT)
        elapsed = time.perf_counter() - start

        times.append(elapsed)
        status_counts[r.status_code] = status_counts.get(r.status_code, 0) + 1

        print(f"Run {i+1:02d}: {elapsed:.3f}s  status={r.status_code}")

    except requests.exceptions.RequestException as e:
        elapsed = time.perf_counter() - start
        status_counts["error"] = status_counts.get("error", 0) + 1
        print(f"Run {i+1:02d}: ERROR after {elapsed:.3f}s  ({e})")

print("\n--- Summary ---")
if times:
    avg = statistics.mean(times)
    med = statistics.median(times)
    mn = min(times)
    mx = max(times)
    p90 = percentile(times, 90)
    p95 = percentile(times, 95)

    print(f"Average: {avg:.3f}s")
    print(f"Median : {med:.3f}s")
    print(f"Min    : {mn:.3f}s")
    print(f"Max    : {mx:.3f}s")
    print(f"P90    : {p90:.3f}s")
    print(f"P95    : {p95:.3f}s")

print("\nStatus counts:", status_counts)
