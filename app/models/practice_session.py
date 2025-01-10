from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PracticeSession(BaseModel):
    id: Optional[int] = None
    start_time: datetime
    end_time: datetime
    personas_total: int
    personas_correct: int
    proceso_total: int
    proceso_correct: int
    entorno_total: int
    entorno_correct: int

    class Config:
        from_attributes = True


class PracticeSessionCreate(BaseModel):
    start_time: datetime
    end_time: datetime
    personas_total: int
    personas_correct: int
    proceso_total: int
    proceso_correct: int
    entorno_total: int
    entorno_correct: int