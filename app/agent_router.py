from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatInput(BaseModel):
    query: str

@router.post("/chat")
def handle_chat(input: ChatInput):
    # For now, echo back the message
    return {"response": f"You said: {input.query}"}
