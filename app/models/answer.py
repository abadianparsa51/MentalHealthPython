from pydantic import BaseModel
from typing import Optional

class Answer(BaseModel):
    id: int
    question_id: Optional[int] = None  # Nullable FK
    answers:  Optional[bool] = None 
    session_id: str
    text: str
