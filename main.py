# # main.py
# from fastapi import FastAPI, Depends, HTTPException, Header
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from pydantic import BaseModel
# import uvicorn

# from app.data.seed_questions import get_seed_questions
# from app.data.seed_answers import get_seed_answers
# from app.data.seed_rules import get_seed_rules
# from app.data.seed_conditions import get_seed_conditions
# from app.evaluators.rule_evaluator import RuleEvaluator
# from app.models.user_answer import UserAnswer

# app = FastAPI(title="NeuroEase Python Service", version="1.0")

# # Security scheme for Bearer token
# security = HTTPBearer()

# # Expected token from configuration
# EXPECTED_TOKEN = "neuroease-python-token"

# # Dependency to verify the token
# async def verify_token(authorization: str = Header(None)):
#     if authorization is None:
#         raise HTTPException(status_code=401, detail="Authorization header missing")
    
#     scheme, token = authorization.split()
#     if scheme.lower() != "bearer":
#         raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    
#     if token != EXPECTED_TOKEN:
#         raise HTTPException(status_code=403, detail="Invalid token")
    
#     return token

# # Example Pydantic model for input data (adjust based on your needs, e.g., for diagnosis or rule evaluation)
# class InputData(BaseModel):
#     answers: dict[str, list[str]]  # دقیقاً مثل C# Answers

#     # Add more fields as needed

# # Example Pydantic model for output data
# class OutputData(BaseModel):
#     diagnosis: str
#     confidence: float
#     # Add more fields as needed

# @app.get("/")
# async def root(token: str = Depends(verify_token)):
#     return {"message": "Welcome to NeuroEase Python Service"}

# # Example endpoint that could be called from ASP.NET Core
# # This simulates processing data (e.g., ML inference) and returning results for ASP.NET to store in DB
# # @app.post("/diagnose", response_model=OutputData)
# # async def diagnose(data: InputData, token: str = Depends(verify_token)):
# #     user_id = data.answers.get("UserId", ["unknown"])[0]
# #     session_id = data.answers.get("SessionId", ["unknown"])[0] 
# #     # جمع‌آوری همه علائم سوالات
# #     symptoms = []
# #     for key, values in data.answers.items():
# #         if key not in ["UserId", "SessionId"]:
# #             symptoms.extend(values)

# #     diagnosis_result = "Potential anxiety disorder" if "1" in symptoms else "No issues detected"
# #     confidence_level = 0.85
# #     return OutputData(diagnosis=diagnosis_result, confidence=confidence_level)

# # if __name__ == "__main__":
# #     uvicorn.run(app, host="0.0.0.0", port=8000)

# @app.post("/diagnose", response_model=OutputData)
# async def diagnose(data: InputData, token: str = Depends(verify_token)):
#     user_id = data.answers.get("UserId", ["unknown"])[0]
#     session_id = data.answers.get("SessionId", ["unknown"])[0]

#     user_answers = []
#     for key, values in data.answers.items():
#         if key not in ["UserId", "SessionId"]:
#             for val in values:
#                 user_answers.append(UserAnswer(question_id=int(key), answer=val, user_id=user_id, session_id=session_id))

#     evaluator = RuleEvaluator(
#         rules=get_seed_rules(),
#         conditions=get_seed_conditions()
#     )

#     result = evaluator.evaluate(user_answers)
#     confidence_level = 0.85
#     return OutputData(diagnosis=result, confidence=confidence_level)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
# main.py
from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from typing import List ,Dict
import uvicorn
import logging
from datetime import datetime

# Import seed data
from app.data.seed_questions import get_seed_questions
from app.data.seed_rules import get_seed_rules
from app.data.seed_conditions import get_seed_conditions
from app.data.seed_answers import get_seed_answers
# Import models
from app.models.user_answer import UserAnswer
from app.evaluators.rule_evaluator import RuleEvaluator

# FastAPI instance
app = FastAPI(title="NeuroEase Python Service", version="1.0")

# Security scheme for Bearer token
security = HTTPBearer()
EXPECTED_TOKEN = "neuroease-python-token"

# Dependency to verify the token
async def verify_token(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    scheme, token = authorization.split()
    if scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    if token != EXPECTED_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return token

# Pydantic models
class InputData(BaseModel):
    answers: dict[str, List[str]]  # {question_id: [answer1, answer2], "UserId": [...], "SessionId": [...]}

class OutputData(BaseModel):
     diagnosis: List[Dict]  # تغییر از str به لیست دیکشنری
     confidence: float

# Load all questions, rules, conditions at startup
all_questions = get_seed_questions()
all_rules = get_seed_rules()
all_conditions = get_seed_conditions()
all_answers = get_seed_answers()

# Root endpoint
@app.get("/")
async def root(token: str = Depends(verify_token)):
    return {"message": "Welcome to NeuroEase Python Service"}

# Diagnose endpoint
@app.post("/diagnose", response_model=OutputData)

async def diagnose(data: InputData, token: str = Depends(verify_token)):
    
    user_id = data.answers.get("UserId", ["unknown"])[0]
    session_id = data.answers.get("SessionId", ["unknown"])[0]

    # تبدیل پاسخ‌ها به لیست UserAnswer
    user_answers = []
    ua_id = 1
    for key, values in data.answers.items():
        if key not in ["UserId", "SessionId"]:
                for val in values:
                    if val in ["1", 1, True]:
                        val_bool = True
                    else:
                        val_bool = False
                    user_answers.append(UserAnswer(
                        id=ua_id,
                        question_id=int(key),
                        answer=val_bool,
                        user_id=user_id,
                        session_id=session_id,
                        created_at=datetime.utcnow()
                    ))
                    ua_id += 1
    # ارزیابی با RuleEvaluator
    evaluator = RuleEvaluator(
        questions=all_questions,
        answers=[],
        rules=all_rules,
        conditions=all_conditions
    )
    result = evaluator.evaluate_user_answers(user_answers)
    logging.debug(f"Diagnosis result: {result}")
    confidence_level = 0.85  # ثابت، می‌توان بعداً ML یا منطق پیچیده اضافه کرد
    if not isinstance(result, list):
        result = []
    return OutputData(diagnosis=result, confidence=confidence_level)

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
