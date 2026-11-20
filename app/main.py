from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, status
from psycopg import Connection

from app.db import get_conn, pool
from app.schemas import TestResult, TestResultCreate

COLUMNS = "id, test_id, test_path, test_module, test_name, status, date, duration"
SCHEMA_SQL = (Path(__file__).parent / "schema.sql").read_text()


@asynccontextmanager
async def lifespan(app: FastAPI):
    pool.open(wait=True)
    with pool.connection() as conn:
        conn.execute(SCHEMA_SQL)
    try:
        yield
    finally:
        pool.close()


app = FastAPI(title="Quality Hub", lifespan=lifespan)


@app.post("/results", response_model=TestResult, status_code=status.HTTP_201_CREATED)
def create_result(payload: TestResultCreate, conn: Connection = Depends(get_conn)):
    return conn.execute(
        f"""
        INSERT INTO test_results (test_id, test_path, test_module, test_name, status, date, duration)
        VALUES (%(test_id)s, %(test_path)s, %(test_module)s, %(test_name)s, %(status)s, COALESCE(%(date)s::timestamptz, now()), %(duration)s)
        RETURNING {COLUMNS}
        """,
        payload.model_dump(),
    ).fetchone()


@app.get("/results", response_model=list[TestResult])
def list_results(conn: Connection = Depends(get_conn)):
    return conn.execute(
        f"SELECT {COLUMNS} FROM test_results ORDER BY date DESC, id DESC"
    ).fetchall()
