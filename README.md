# 🏥 Clinical AI Assistant

An AI-powered backend that processes doctor–patient transcripts and generates structured clinical insights using Large Language Models (LLMs).

Deployed on **Render**, secured with **API key authentication**, and includes a **latency benchmarking** script for performance measurement.

---

## 🚀 Live Deployment

**API Base URL**
- https://clinical-ai-assistant-61ui.onrender.com

> Note: The `/generate` endpoint is protected. You must send a valid `X-API-KEY` header.

---

## ✨ Key Features

- 🧠 Converts raw medical conversations into structured outputs
- 🔐 API key authentication via `X-API-KEY`
- ☁️ Hosted on Render (cloud deployment)
- 📊 Latency benchmarking script included (`metrics/benchmark_latency.py`)
- 🧪 Simple REST endpoint for transcript processing
- 🛡️ Secrets handled via environment variables (`.env`) — no hardcoded keys

---

## 🧱 Tech Stack

- **Python 3.10+**
- Backend framework: **FastAPI / Flask** *(update this to whichever you used)*
- **OpenAI API** (LLM inference)
- **Render** (deployment)
- `python-dotenv` (env management)
- `requests` (benchmark script)

---

## 🗂️ Project Structure (Typical)

> Your repo may vary slightly—update if needed.

```text
Clinical_AI_Assistant/
│
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── services/
│   ├── requirements.txt
│   └── .env                # NOT committed (local only)
│
├── metrics/
│   └── benchmark_latency.py
│
├── .gitignore
└── README.md
```
---

## 🔐 Authentication

All requests to protected endpoints (e.g., `/generate`) must include a valid API key in the request header.

### Required Header

`X-API-KEY: <your_api_key>`

If the API key is missing or incorrect, the server will return **401 Unauthorized**.

---

## 📡 API Reference

### POST `/generate`

#### Headers
```json
{
  "Content-Type": "application/json",
  "X-API-KEY": "your_api_key"
}
```

#### Body
```json
{
  "text": "Doctor: What brings you in today? Patient: I have fever and cough..."
}
```

#### Example cURL
```bash
curl -X POST https://clinical-ai-assistant-61ui.onrender.com/generate \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: your_api_key" \
  -d '{"text":"Doctor: What brings you in today? Patient: I have fever and cough."}'
```

---

## 🧪 Local Setup

### 1) Clone the repository
```bash
git clone https://github.com/Amit-Kumar-KJ/Clinical_AI_Assistant.git
cd Clinical_AI_Assistant
```

### 2) Create & activate a virtual environment

Recommended: create the venv inside `backend/` since backend dependencies live there.

```bash
cd backend
python -m venv venv
```

Windows (PowerShell)
```bash
venv\Scripts\Activate.ps1
```

Windows (CMD)
```bash
venv\Scripts\activate.bat
```

macOS/Linux
```bash
source venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Create a `.env` file (IMPORTANT)

Create `backend/.env`:

```env
APP_API_KEY=your_secret_key_for_this_app
OPENAI_API_KEY=your_openai_key
```

Keep `.env` local only.  
Never commit `.env` to GitHub.

### 5) Run the backend

Replace the run command if your project uses uvicorn/FastAPI, etc.

If Flask-style
```bash
python app.py
```

If FastAPI + uvicorn
```bash
uvicorn app:app --reload
```

---

## 📊 Benchmarking (Latency Metrics)

This project includes a benchmarking script:

`metrics/benchmark_latency.py`

### Run benchmark

From repo root:
```bash
python metrics/benchmark_latency.py
```

Or:
```bash
cd metrics
python benchmark_latency.py
```

### What it measures

- Average latency  
- Min latency  
- Max latency  
- Standard deviation (jitter)  

Tip: Run at least 20–50 requests for a stable average, especially on Render free tier.

---

## 🧾 Resume-Ready Metrics Line

You can add a bullet like this (replace X with your benchmark result):

Deployed an AI-powered clinical transcript processing backend on Render, achieving ~X seconds average response latency per transcript request, secured via API-key authentication and environment-based secret management.

---

## 🛡️ Security Notes

- API keys stored in environment variables  
- `.env` is ignored via `.gitignore`  
- Requests require `X-API-KEY` header  
- No secrets are hardcoded into source code  

---

## 🗺️ Roadmap / Future Improvements

- Add rate limiting (protect from abuse)  
- Add request logging + analytics dashboard  
- Add structured JSON output schema (validated)  
- Add Docker support + production config  
- Add CI/CD (GitHub Actions)  
- Add caching for frequent requests  
- Add unit tests & integration tests  

---

## 👨‍💻 Author

Amit Kumar  
GitHub: https://github.com/Amit-Kumar-KJ  

---

## ⭐ Support

If you find this project helpful, consider giving it a star on GitHub!