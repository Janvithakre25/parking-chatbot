# Smart Parking Chatbot

Chatbot microservice for the Smart Parking website.

## Architecture
```
Chat UI (test_widget.html / your real frontend)
    -> POST /chat  (main.py)
        -> intent.py        detects what the user wants
        -> mock_data.py     fetches facts (SWAP for real backend API later)
        -> llm_service.py   phrases the reply naturally (LLM optional)
```

The LLM never invents availability/price data — it only phrases whatever
`mock_data.py` (soon: the real backend) returns. This keeps answers accurate.

## Setup
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Server runs at http://localhost:8000. Open `test_widget.html` in a browser to chat with it.

### Optional: enable real LLM phrasing
```bash
export ANTHROPIC_API_KEY=your_key_here
```
Without a key, the bot still works using template responses (see `llm_service.py`).

## Try it
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "any vacant spots near Gate 2?"}'
```

## When the real backend is ready
Open `mock_data.py`. Replace the body of each function with a call to the
actual backend endpoint, keeping the same function name and return shape:

```python
def get_available_slots(location=None):
    resp = httpx.get(f"{BACKEND_URL}/api/slots/available", params={"location": location})
    return resp.json()
```

Nothing in `main.py`, `intent.py`, or `llm_service.py` needs to change.

## Files
- `main.py` — FastAPI app, `/chat` endpoint
- `intent.py` — keyword-based intent detection
- `mock_data.py` — temporary stand-in for backend/DB (swap later)
- `llm_service.py` — phrases replies via Claude API, with template fallback
- `test_widget.html` — standalone browser test page
- `requirements.txt`

## Next steps (backlog, not this week)
- Swap mock_data.py for real backend calls once ready
- Improve intent detection (embeddings-based instead of keyword)
- Add session/conversation memory
- Deploy (Render/Railway for the API, same host as frontend or separate)