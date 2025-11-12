from app.models.answer import Answer

def get_seed_answers():
    return [
        Answer(id=1, text="yes", answers=True, session_id="SeedSession1", question_id=1),
        Answer(id=2, text="no",  answers=False, session_id="SeedSession1", question_id=1),
        Answer(id=3, text="yes", answers=True, session_id="SeedSession1", question_id=2),
        Answer(id=4, text="no",  answers=False, session_id="SeedSession1", question_id=2),
        Answer(id=5, text="yes", answers=True, session_id="SeedSession1", question_id=10),
        Answer(id=6, text="no",  answers=False, session_id="SeedSession1", question_id=10),
        Answer(id=7, text="yes", answers=True, session_id="SeedSession1", question_id=15),
        Answer(id=8, text="no",  answers=False, session_id="SeedSession1", question_id=15),
    ]
