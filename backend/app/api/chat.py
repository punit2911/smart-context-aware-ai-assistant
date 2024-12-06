# app/api/chat.py

from fastapi import APIRouter
from pydantic import BaseModel  # <-- Import BaseModel from Pydantic
from transformers import pipeline
from app.api.memory import memory  # Avoid circular imports

router = APIRouter()

# Initialize the conversational model
chat_pipeline = pipeline("text-generation", model="gpt2")  # Example model

# Define the Message schema using Pydantic
class Message(BaseModel):  # <-- Now we can use BaseModel
    message: str

# Endpoint to handle the user's message
@router.post("/send")
async def send_message(message: Message):
    # Process the message and get a response
    user_message = message.message
    print(f"User message: {user_message}")

    # Generate the bot's response
    bot_response = chat_pipeline(user_message, max_length=50, num_return_sequences=1)[0]['generated_text']

    # Add message to memory
    memory.append({"user_message": user_message, "bot_response": bot_response})

    return {"response": bot_response}

