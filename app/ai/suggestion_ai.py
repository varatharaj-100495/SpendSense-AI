def generate_suggestion(
    amount: float,
    category: str
):

    if category == "Food" and amount > 300:
        return (
            "You spent a relatively high amount on food today. "
            "Consider cooking at home to save money."
        )

    if category == "Transport" and amount > 800:
        return (
            "Transport expense is quite high. "
            "If possible, combine trips or use public transport."
        )

    if category == "Entertainment" and amount > 500:
        return (
            "Entertainment spending is above your usual daily limit. "
            "Keep an eye on discretionary expenses."
        )

    return "Good job! Your spending looks reasonable."