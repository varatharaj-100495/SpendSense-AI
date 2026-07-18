from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.expense import Expense
from app.models.budget import Budget


def get_dashboard(db: Session):

    expenses = db.query(Expense).all()
    budget = db.query(Budget).first()

    total_expense = sum(expense.amount for expense in expenses)

    total_transactions = len(expenses)

    top_category_query = (
        db.query(
            Expense.category,
            func.count(Expense.category).label("count")
        )
        .group_by(Expense.category)
        .order_by(func.count(Expense.category).desc())
        .first()
    )

    top_category = (
        top_category_query.category
        if top_category_query
        else "No Data"
    )

    latest_expense = (
        db.query(Expense)
        .order_by(Expense.created_at.desc())
        .first()
    )

    latest_ai_suggestion = (
        "No suggestions available"
        if latest_expense is None
        else (
            f"Latest expense '{latest_expense.description}' "
            f"was categorized as {latest_expense.category}."
        )
    )

    weekly_budget = budget.weekly_limit if budget else 0
    monthly_budget = budget.monthly_limit if budget else 0

    remaining_weekly_budget = max(
        weekly_budget - total_expense,
        0
    )

    remaining_monthly_budget = max(
        monthly_budget - total_expense,
        0
    )

    budget_used_percentage = 0

    if weekly_budget > 0:
        budget_used_percentage = round(
            (total_expense / weekly_budget) * 100,
            2
    )

    return {
        "total_expense": total_expense,
        "total_transactions": total_transactions,
        "top_category": top_category,
        "latest_ai_suggestion": latest_ai_suggestion,

        "weekly_budget": weekly_budget,
        "monthly_budget": monthly_budget,
        "remaining_weekly_budget": remaining_weekly_budget,
        "budget_used_percentage": budget_used_percentage,
    }