from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Question(BaseModel):
    id: int
    section: str
    text: str
    order: int
    created_at: datetime
