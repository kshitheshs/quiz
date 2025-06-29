from pydantic import BaseModel
from typing import List, Optional

game_id: Optional[str] = None

class User(BaseModel):
    user_id: str
    subject: str

class MatchResponse(BaseModel):
    status: str
    game_id: Optional[str] = None
    teammate: Optional[str] = None
    opponents: Optional[List[str]] = None

class AnswerSubmission(BaseModel):
    game_id: str
    user_id: str
    question_id: str
    answer: str
    timestamp: float
