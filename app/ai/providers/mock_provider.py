import json


class MockProvider:

    def generate(self, prompt: str):

        response = {
            "risk": "Medium",
            "summary": (
                "Food spending is increasing compared "
                "to your recent expenses."
            ),
            "tip": (
                "Reduce restaurant spending this week "
                "to stay within budget."
            ),
        }

        return json.dumps(response)