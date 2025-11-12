from typing import List
from app.models.question import Question
from app.models.answer import Answer
from app.models.diagnostic_rule import DiagnosticRule
from app.models.rule_condition import RuleCondition
from app.models.user_answer import UserAnswer

class RuleEvaluator:
    def __init__(self, questions: List[Question], answers: List[Answer],
                 rules: List[DiagnosticRule], conditions: List[RuleCondition]):
        self.questions = {q.id: q for q in questions}
        self.answers = answers
        self.rules = {r.id: r for r in rules}
        self.conditions = conditions

        # attach conditions to rules
        for condition in conditions:
            rule = self.rules.get(condition.diagnostic_rule_id)
            if rule:
                if not hasattr(rule, "conditions") or rule.conditions is None:
                    rule.conditions = []
                rule.conditions.append(condition)

    def evaluate_user_answers(self, user_answers: List[UserAnswer]):
        """
        بررسی پاسخ‌های کاربر و بازگشت لیست تشخیص‌ها
        """
        results = []

        # map answers by question_id for fast lookup
        user_answer_map = {ua.question_id: ua.answer for ua in user_answers}

        for rule in self.rules.values():
            matched_count = 0
            for condition in rule.conditions:
                expected = condition.expected_answer
                user_resp = user_answer_map.get(condition.question_id)
                if user_resp == expected:
                    matched_count += 1

            if matched_count >= rule.minimum_matches_required:
                results.append({
                    "code": rule.code,
                    "title": rule.title,
                    "matched": matched_count,
                    "required": rule.minimum_matches_required
                })

        return results
