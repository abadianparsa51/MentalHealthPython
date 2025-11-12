from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from .rule_condition import RuleCondition

class DiagnosticRule(BaseModel):
    id: int
    code: str
    title: str
    description: Optional[str] = None
    minimum_matches_required: int
    conditions: Optional[List[RuleCondition]] = []
    created_at: datetime
