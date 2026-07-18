from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.expense import Expense
from app.models.budget import Budget

from app.ai.ai_service import AIService

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post("/analyze")
def analyze_finances(
    db: Session = Depends(get_db),
):

    expenses = (
        db.query(Expense)
        .order_by(Expense.created_at.desc())
        .limit(20)
        .all()
    )

    budget = db.query(Budget).first()

    ai_service = AIService()

    return ai_service.generate_financial_advice(
        expenses,
        budget,
    )