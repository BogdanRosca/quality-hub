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
  -d '{"test_id": "057c387a-a78a-4007-8888-6db23da22c5a", "test_module": "tests/test_auth.py", "test_name": "test_login", "test_path": "tests/test_auth.py::test_login", "status": "passed", "duration": 1.234}'

curl localhost:8000/results
```

`status` must be one of `passed`, `failed`, `skipped`. `duration` is in seconds (>= 0).
`date` is optional and defaults to the current time.
