import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

load_dotenv()


class GeminiProvider:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )
        self.model = "gemini-2.0-flash"

    def generate(self, prompt):

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            return response.text


        except ClientError as e:

            print("Gemini API Error:", e)

            if e.code == 429:
                return {
                    "error": "AI quota exceeded. Please try again later."
                }

            if e.code == 404:
                return {
                    "error": "AI model unavailable."
                }

            return {
                "error": "Gemini service error."
            }


        except Exception as e:

            print("Unexpected AI Error:", e)

            return {
                "error": "AI service temporarily unavailable."
            }