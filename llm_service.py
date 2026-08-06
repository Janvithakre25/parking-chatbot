import os

try:
    import anthropic
    _client = anthropic.Anthropic() if os.environ.get("ANTHROPIC_API_KEY") else None
except ImportError:
    _client = None

def generate_reply(user_message: str, intent: str, context_data: dict) -> str:
    if _client:
        system_prompt = (
            "You are a helpful assistant for a Smart Parking website. "
            "Answer the user's question in 1-3 friendly sentences. "
            "ONLY use the facts given in CONTEXT DATA below — never invent "
            "slot numbers, prices, or availability that isn't in the context. "
            "If context data is empty, politely say you don't have that info."
        )
        user_prompt = (
            f"User message: {user_message}\n"
            f"Detected intent: {intent}\n"
            f"CONTEXT DATA: {context_data}\n"
        )
        try:
            response = _client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=200,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}],
            )
            return response.content[0].text
        except Exception:
            pass

    return _template_reply(intent, context_data)


def _template_reply(intent: str, data: dict) -> str:
    if intent == "greeting":
        return "Hi there! 👋 I can help you find parking, check rates, or answer questions. What do you need?"
    if intent == "availability":
        slots = data.get("slots", [])
        if not slots:
            return "Sorry, no vacant slots right now. Please check back shortly."
        lines = [f"{s['id']} at {s['location']} (₹{s['price_per_hr']}/hr)" for s in slots]
        return "Here are the vacant slots: " + ", ".join(lines)
    if intent == "booking":
        result = data.get("booking_result")
        if result and result.get("success"):
            return f"Booked slot {result['slot']['id']} at {result['slot']['location']}. See you soon!"
        return "Sorry, I couldn't book that slot — it may already be taken. Try another one."
    if intent in ("rates", "hours", "payment", "cancellation"):
        answer = data.get("faq_answer")
        return answer or "I don't have that info handy — please check the FAQ page."
    return "I'm not sure I understood that. You can ask me about parking availability, rates, or bookings."