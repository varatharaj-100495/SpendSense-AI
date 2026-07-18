from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.budget_schema import BudgetCreate
from app.services.budget_service import (
    create_or_update_budget,
    get_budget
)

router = APIRouter(
    prefix="/budget",
    tags=["Budget"]
)


@router.post("")
def save_budget(
    budget: BudgetCreate,
    db: Session = Depends(get_db)
):
    return create_or_update_budget(db, budget)


@router.get("")
def fetch_budget(
    db: Session = Depends(get_db)
):
    return get_budget(db)