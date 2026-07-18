from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.expense import Expense
from app.models.budget import Budget
from app.models.chat_message import ChatMessage

from app.schemas.chat_schema import ChatRequest

from app.ai.services.ai_chat_service import AIChatService


router = APIRouter(
    prefix="/ai",
    tags=["AI Chat"]
)


@router.post("/chat")
def chat_with_ai(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    try:

        expenses = (
            db.query(Expense)
            .order_by(
                Expense.created_at.desc()
            )
            .limit(20)
            .all()
        )


        budget = db.query(Budget).first()


        ai_service = AIChatService()


        response = ai_service.chat(
            db=db,
            message=request.message,
            expenses=expenses,
            budget=budget
        )


        return response


    except Exception as e:

        print("AI Chat Error:", e)

        raise HTTPException(
            status_code=500,
            detail="AI chat service failed"
        )



@router.get("/history")
def get_chat_history(
    db: Session = Depends(get_db)
):

    chats = (
        db.query(ChatMessage)
        .order_by(
            ChatMessage.created_at.asc()
        )
        .all()
    )


    return [
        {
            "id": chat.id,
            "user_message": chat.user_message,
            "ai_response": chat.ai_response,
            "created_at": chat.created_at
        }
        for chat in chats
    ]