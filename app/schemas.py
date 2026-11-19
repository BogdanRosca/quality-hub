from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

Status = Literal["pass", "failed", "skipped"]


class TestResultCreate(BaseModel):
    name: str = Field(min_length=1)
    status: Status
    duration: float = Field(ge=0, description="Duration in seconds")
    date: datetime | None = None


class TestResult(TestResultCreate):
    id: int
    date: datetime
