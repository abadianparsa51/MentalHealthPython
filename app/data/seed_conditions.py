from app.models.rule_condition import RuleCondition

conditions = [
    RuleCondition(id=1, diagnostic_rule_id=1, question_id=1, expected_answer="yes"),
    RuleCondition(id=2, diagnostic_rule_id=1, question_id=2, expected_answer="yes"),
    RuleCondition(id=3, diagnostic_rule_id=1, question_id=3, expected_answer="yes"),
    RuleCondition(id=4, diagnostic_rule_id=1, question_id=4, expected_answer="yes"),
    RuleCondition(id=5, diagnostic_rule_id=1, question_id=5, expected_answer="yes"),
    RuleCondition(id=6, diagnostic_rule_id=2, question_id=9, expected_answer="yes"),
    RuleCondition(id=7, diagnostic_rule_id=2, question_id=10, expected_answer="yes"),
    RuleCondition(id=8, diagnostic_rule_id=2, question_id=11, expected_answer="yes"),
    RuleCondition(id=9, diagnostic_rule_id=3, question_id=15, expected_answer="yes"),
    RuleCondition(id=10, diagnostic_rule_id=3, question_id=16, expected_answer="yes"),
    RuleCondition(id=11, diagnostic_rule_id=4, question_id=17, expected_answer="yes"),
    RuleCondition(id=12, diagnostic_rule_id=4, question_id=18, expected_answer="yes")
]

def get_seed_conditions():
    """بازگرداندن لیست شرایط قانونی"""
    return conditions