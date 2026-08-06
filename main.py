from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from intent import detect_intent
from llm_service import generate_reply
import mock_data

app = FastAPI(title="Smart Parking Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None

class ChatResponse(BaseModel):
    reply: str
    intent: str

@app.get("/")
def health_check():
    return {"status": "ok", "service": "parking-chatbot"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    intent = detect_intent(req.message)
    context_data = {}

    if intent == "availability":
        location = _extract_location(req.message)
        context_data["slots"] = mock_data.get_available_slots(location)
    elif intent == "booking":
        slot_id = _extract_slot_id(req.message)
        if slot_id:
            context_data["booking_result"] = mock_data.book_slot(slot_id)
        else:
            context_data["booking_result"] = {"success": False, "reason": "No slot ID provided"}
    elif intent in ("rates", "hours", "payment", "cancellation"):
        context_data["faq_answer"] = mock_data.get_faq_answer(intent)

    reply = generate_reply(req.message, intent, context_data)
    return ChatResponse(reply=reply, intent=intent)

def _extract_location(message: str) -> str | None:
    for loc in ["gate 1", "gate 2", "basement"]:
        if loc in message.lower():
            return loc
    return None

def _extract_slot_id(message: str) -> str | None:
    import re
    match = re.search(r"\b([A-Za-z]\d)\b", message)
    return match.group(1).upper() if match else None