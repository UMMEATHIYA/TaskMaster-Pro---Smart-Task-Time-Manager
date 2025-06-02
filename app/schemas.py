from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskResponse(TaskCreate):
    id: int
    is_completed: bool
    created_at: datetime

    class Config:
        orm_mode = True
