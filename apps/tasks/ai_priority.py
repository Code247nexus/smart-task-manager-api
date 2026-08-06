def predict_priority(title, description):

    text = f"{title} {description}".lower()

    high = [
        "urgent",
        "asap",
        "deadline",
        "critical",
        "important",
        "today",
    ]

    medium = [
        "meeting",
        "review",
        "assignment",
        "project",
    ]

    for word in high:
        if word in text:
            return "HIGH"

    for word in medium:
        if word in text:
            return "MEDIUM"

    return "LOW"