# GuardianGrid - Local Emergency Support System

A crisis response platform enabling rapid coordination of relief efforts, resource allocation, and community support during emergencies.

## Tech Stack
- FastAPI
- SQLite (SQLAlchemy)
- Uvicorn

## Quickstart

```bash
# 1) Create a virtualenv (optional)
python -m venv .venv && source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the API
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 4) Check health
curl http://localhost:8000/api/v1/health
```

## Roadmap
- Incidents reporting and verification
- Resource inventory management
- Geolocation-based help matching
- Crowd-sourced damage assessments
- Family reunification
- Mental health resource directory
- Post-crisis recovery project tracking
- i18n and offline-friendly endpoints
