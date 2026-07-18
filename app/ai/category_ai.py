def predict_category(description: str):

    text = description.lower()


    if any(word in text for word in [
        "petrol",
        "fuel",
        "bike",
        "car",
        "bus"
    ]):
        return "Transport"


    if any(word in text for word in [
        "food",
        "lunch",
        "dinner",
        "tea",
        "coffee"
    ]):
        return "Food"


    if any(word in text for word in [
        "movie",
        "game",
        "netflix"
    ]):
        return "Entertainment"


    return "Others"