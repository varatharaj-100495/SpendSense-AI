from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime

from app.database.base import Base


class Budget(Base):

    __tablename__ = "budgets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    weekly_limit = Column(
        Float,
        nullable=False
    )

    monthly_limit = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )