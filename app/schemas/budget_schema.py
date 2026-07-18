from pydantic import BaseModel


class BudgetCreate(BaseModel):
    weekly_limit: float
    monthly_limit: float


class BudgetResponse(BaseModel):
    id: int
    weekly_limit: float
    monthly_limit: float

    class Config:
        from_attributes = True