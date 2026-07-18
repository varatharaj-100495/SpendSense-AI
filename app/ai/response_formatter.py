import json


class ResponseFormatter:

    @staticmethod
    def format(response: str):

        try:
            return json.loads(response)

        except json.JSONDecodeError:

            return {
                "risk": "Unknown",
                "summary": "Unable to analyze expenses.",
                "tip": "Please try again."
            }