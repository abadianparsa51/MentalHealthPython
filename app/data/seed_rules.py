from datetime import datetime
from app.models.diagnostic_rule import DiagnosticRule

static_date = datetime(2025, 1, 1)

rules = [
    DiagnosticRule(
        id=1,
        code="DEP001",
        title="اختلال افسردگی عمده",
        description="بر اساس پاسخ به سوالات مربوط به معیارهای افسردگی (حداقل 5 علامت شامل غمگینی یا بی‌علاقگی).",
        minimum_matches_required=5,
        created_at=static_date
    ),
    DiagnosticRule(
        id=2,
        code="HYP001",
        title="هیپومانیا",
        description="بر اساس پاسخ به سوالات مربوط به معیارهای هیپومانیا (حداقل 3 علامت).",
        minimum_matches_required=3,
        created_at=static_date
    ),
    DiagnosticRule(
        id=3,
        code="MAN001",
        title="مانیا",
        description="بر اساس پاسخ به سوالات مربوط به معیارهای مانیا (خلق بالا و رفتار مشکل‌ساز).",
        minimum_matches_required=2,
        created_at=static_date
    ),
    DiagnosticRule(
        id=4,
        code="PAN001",
        title="اختلال پانیک",
        description="بر اساس پاسخ به سوالات مربوط به حملات پانیک و نگرانی از تکرار آن‌ها.",
        minimum_matches_required=2,
        created_at=static_date
    )
]
def get_seed_rules():
    """بازگرداندن لیست قوانین تشخیصی"""
    return rules