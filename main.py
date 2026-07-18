from fastapi import FastAPI

from app.api.expense import router as expense_router
from app.database.base import Base
from app.database.database import engine
from app.api.dashboard import router as dashboard_router
from app.api.budget import router as budget_router
from app.api.ai import router as ai_router
from app.api.ai_chat import router as ai_chat_router
from fastapi.middleware.cors import CORSMiddleware


import app.models.expense
import app.models.budget
import app.models.chat_message

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SpendSense AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expense_router)
app.include_router(dashboard_router)
app.include_router(budget_router)
app.include_router(ai_router)
app.include_router(ai_chat_router)


@app.get("/")
def root():
    return {
        "message": "SpendSense AI Backend Running 🚀"
    }