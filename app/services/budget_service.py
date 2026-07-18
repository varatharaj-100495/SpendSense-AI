from sqlalchemy.orm import Session

from app.models.budget import Budget
from app.schemas.budget_schema import BudgetCreate


def create_or_update_budget(
    db: Session,
    budget: BudgetCreate
):
    existing_budget = db.query(Budget).first()

    if existing_budget:

        existing_budget.weekly_limit = budget.weekly_limit
        existing_budget.monthly_limit = budget.monthly_limit

        db.commit()
        db.refresh(existing_budget)

        return existing_budget

    new_budget = Budget(
        weekly_limit=budget.weekly_limit,
        monthly_limit=budget.monthly_limit
    )

    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)

    return new_budget


def get_budget(db: Session):

    budget = db.query(Budget).first()

    return budget