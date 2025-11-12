from pydantic import BaseModel

class RuleCondition(BaseModel):
    id: int
    diagnostic_rule_id: int
    question_id: int
    expected_answer: str
