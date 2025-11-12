from pydantic import BaseModel
from datetime import datetime

class Diagnosis(BaseModel):
    id: int
    session_id: str
    result: str
    diagnostic_rule_id: int
    code: str
    title: str
    created_at: datetime
    user_id: str
