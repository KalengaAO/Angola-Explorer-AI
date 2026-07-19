from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from explorerAI.database import get_db

from .recommendation_agent import RecommendationAgent


router = APIRouter(
    prefix="/agents",
    tags=["agents"]
)


class RecommendationRequest(BaseModel):
    question: str


agent = RecommendationAgent()


@router.post("/recommend")
def recommend(
    request: RecommendationRequest,
    db: Session = Depends(get_db)
):
    return agent.run(
        question=request.question,
        db=db
    )