from pydantic import BaseModel, Field
import random
from datetime import datetime

class UserAnswer(BaseModel):
    id: int = Field(default_factory=lambda: random.randint(1000, 9999))
    question_id: int
    answer: str       # این باید رشته باشه
    user_id: str
    session_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
