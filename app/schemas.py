from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field

Status = Literal["passed", "failed", "skipped"]


class TestResultCreate(BaseModel):
    test_id: UUID
    test_path: str = Field(min_length=1)
    test_module: str = Field(min_length=1)
    test_name: str = Field(min_length=1)
    status: Status
    duration: float = Field(ge=0, description="Duration in seconds")
    date: datetime | None = None


class TestResult(TestResultCreate):
    id: int
    date: datetime
