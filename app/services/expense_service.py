from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.schemas.expense_schema import ExpenseCreate
from app.ai.category_ai import predict_category
from app.ai.suggestion_ai import generate_suggestion


def create_expense(db: Session, expense: ExpenseCreate):
    category = predict_category(
        expense.description
    )
    suggestion = generate_suggestion(
        expense.amount,
        category
    )

    new_expense = Expense(
        amount=expense.amount,
        description=expense.description,
        category=category
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return {
        "success": True,
        "message": "Expense added successfully",
        "data": {
            "id": new_expense.id,
            "amount": new_expense.amount,
            "description": new_expense.description,
            "category": new_expense.category,
            "suggestion": suggestion
        }
    }


def get_expenses(db: Session):
    expenses = db.query(Expense).all()

    return {
        "success": True,
        "message": "Expenses fetched successfully",
        "data": [
            {
                "id": expense.id,
                "amount": expense.amount,
                "description": expense.description,
                "category": expense.category,
            }
            for expense in expenses
        ]
    }