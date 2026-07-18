from app.models.expense import Expense
from app.models.budget import Budget


def build_financial_prompt(
    expenses: list[Expense],
    budget: Budget,
):
    expense_lines = []

    for expense in expenses:
        expense_lines.append(
            f"- {expense.description} | "
            f"₹{expense.amount} | "
            f"{expense.category}"
        )

    expense_text = "\n".join(expense_lines)

    prompt = f"""
You are an expert AI Financial Coach.

Your job is to analyze a user's expenses and provide practical financial advice.

Current Weekly Budget:
₹{budget.weekly_limit if budget else 0}

Current Monthly Budget:
₹{budget.monthly_limit if budget else 0}

Recent Expenses:

{expense_text}

Instructions:

1. Analyze spending habits.
2. Mention the biggest spending category.
3. Suggest ONE realistic saving idea.
4. Mention the financial risk level:
   Low / Medium / High
5. Keep the response under 80 words.

Return ONLY valid JSON.

Example:

{{
    "risk":"Medium",
    "summary":"Food spending is increasing.",
    "tip":"Reduce restaurant visits this week."
}}
"""

    return prompt