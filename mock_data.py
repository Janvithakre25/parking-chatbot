from datetime import datetime

SLOTS = [
    {"id": "A1", "location": "Gate 1", "status": "occupied", "price_per_hr": 20},
    {"id": "A2", "location": "Gate 1", "status": "vacant", "price_per_hr": 20},
    {"id": "B1", "location": "Gate 2", "status": "vacant", "price_per_hr": 25},
    {"id": "B2", "location": "Gate 2", "status": "occupied", "price_per_hr": 25},
    {"id": "C1", "location": "Basement", "status": "vacant", "price_per_hr": 15},
    {"id": "C2", "location": "Basement", "status": "vacant", "price_per_hr": 15},
]

FAQS = {
    "rates": "Parking rates range from ₹15/hr (Basement) to ₹25/hr (Gate 2), depending on location.",
    "hours": "The parking facility is open 24/7.",
    "payment": "We accept UPI, cards, and cash at the entry gate.",
    "cancellation": "You can cancel a booking free of charge up to 15 minutes before your slot time.",
}

def get_available_slots(location: str | None = None):
    results = [s for s in SLOTS if s["status"] == "vacant"]
    if location:
        results = [s for s in results if location.lower() in s["location"].lower()]
    return results

def book_slot(slot_id: str):
    for s in SLOTS:
        if s["id"] == slot_id and s["status"] == "vacant":
            s["status"] = "occupied"
            return {"success": True, "slot": s, "booked_at": datetime.now().isoformat()}
    return {"success": False, "reason": "Slot unavailable or does not exist"}

def get_faq_answer(topic: str):
    return FAQS.get(topic)