INTENT_KEYWORDS = {
    "greeting": ["hi", "hello", "hey", "good morning", "good evening"],
    "availability": ["vacant", "available", "free slot", "empty", "space", "parking spot", "any spot"],
    "booking": ["book", "reserve", "reservation"],
    "rates": ["price", "rate", "cost", "how much", "charges"],
    "hours": ["open", "timing", "hours", "close"],
    "payment": ["pay", "payment", "upi", "card", "cash"],
    "cancellation": ["cancel", "refund"],
}

def detect_intent(message: str) -> str:
    text = message.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return intent
    return "fallback"