from app.ai.prompts.chat_prompt import build_chat_prompt
from app.ai.providers.gemini_provider import GeminiProvider


from app.models.chat_message import ChatMessage


class AIChatService:

    def __init__(self):
        self.provider = GeminiProvider()


    def chat(
        self,
        db,
        message,
        expenses,
        budget
    ):

        prompt = build_chat_prompt(
            message,
            expenses,
            budget
        )


        response = self.provider.generate(
            prompt
        )


        chat = ChatMessage(
            user_message=message,
            ai_response=response
        )


        db.add(chat)
        db.commit()
        db.refresh(chat)


        return {
            "id": chat.id,
            "answer": response,
            "created_at": chat.created_at
        }