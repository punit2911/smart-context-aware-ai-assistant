# app/api/memory.py

from fastapi import APIRouter

router = APIRouter()

# A simple in-memory list to store chat history (should be replaced with a database for persistence in production)
memory = []

# Endpoint to retrieve conversation history
@router.get("/history")
async def get_memory():
    if memory:
        return {"memory": memory}
    else:
        return {"message": "No conversation history available."}

# Endpoint to clear the memory (optional feature)
@router.delete("/clear")
async def clear_memory():
    memory.clear()
    return {"message": "Memory cleared."}
