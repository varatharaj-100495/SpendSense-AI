import os

from dotenv import load_dotenv

from app.ai.prompt_builder import build_financial_prompt
from app.ai.response_formatter import ResponseFormatter

from app.ai.providers.mock_provider import MockProvider
from app.ai.providers.gemini_provider import GeminiProvider

load_dotenv()


class AIService:

    def __init__(self):

        provider = os.getenv("AI_PROVIDER", "mock")

        if provider == "gemini":
            self.provider = GeminiProvider()
        else:
            self.provider = MockProvider()

    def generate_financial_advice(
        self,
        expenses,
        budget,
    ):

        prompt = build_financial_prompt(
            expenses,
            budget,
        )

        response = self.provider.generate(
            prompt
        )

        return ResponseFormatter.format(
            response
        )