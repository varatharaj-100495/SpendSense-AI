from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.expense_schema import ExpenseCreate
from app.services.expense_service import create_expense, get_expenses

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post("")
def add_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db)
):
    return create_expense(db, expense)


@router.get("")
def fetch_expenses(
    db: Session = Depends(get_db)
):
    return get_expenses(db)