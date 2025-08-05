# app/main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.agent import ask_agent

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Agentic AI Chatbot is running"}

@app.post("/chat")
def chat(chat_request: ChatRequest):
    response = ask_agent(chat_request.query)
    return {"response": response}