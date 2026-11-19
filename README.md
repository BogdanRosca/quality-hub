# quality-hub

FastAPI service that stores and lists test results in the `quality-db` Postgres database.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # adjust DATABASE_URL if needed
```

## Run

```bash
uvicorn app.main:app --reload
```

Interactive docs: http://localhost:8000/docs

## Endpoints

| Method | Path       | Description                    |
|--------|------------|--------------------------------|
| POST   | `/results` | Add a test result (201)        |
| GET    | `/results` | List all results, newest first |

```bash
curl -X POST localhost:8000/results \
  -H 'Content-Type: application/json' \
  -d '{"name": "login works", "status": "pass", "duration": 1.234}'

curl localhost:8000/results
```

`status` must be one of `pass`, `failed`, `skipped`. `duration` is in seconds (>= 0).
`date` is optional and defaults to the current time.
