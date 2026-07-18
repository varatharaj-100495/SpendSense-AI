def build_chat_prompt(
    message,
    expenses,
    budget
):

    expense_context = "\n".join(
        [
            f"{expense.description}: ₹{expense.amount}"
            for expense in expenses
        ]
    )

    prompt = f"""
You are SpendSense AI, a personal finance assistant.

User question:
{message}


Recent expenses:
{expense_context}


Budget:
Weekly limit: {budget.weekly_limit if budget else "Not set"}
Monthly limit: {budget.monthly_limit if budget else "Not set"}


Instructions:
- Give practical financial advice.
- Keep the answer simple.
- Use the user's spending data.
- Do not invent transactions.
"""

    return prompt