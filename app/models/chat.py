from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    message: str
    max_tokens: Optional[int] = 4096
    temperature: Optional[float] = 0.7

class ChatResponse(BaseModel):
    response: str
    usage: dict