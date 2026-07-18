from sqlalchemy import Column, Float, Integer, String, DateTime
from datetime import datetime

from app.database.base import Base


class Expense(Base):

    __tablename__ = "expenses"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    amount = Column(
        Float,
        nullable=False
    )


    description = Column(
        String,
        nullable=False
    )


    category = Column(
        String,
        nullable=False,
        default="Others"
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )