from fastapi import APIRouter, Depends, HTTPException, Header, status
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import chat_service
from app.services.auth_service import auth_service

router = APIRouter()


@router.post("/", response_model=ChatResponse)
async def chat_with_gpt(
        request: ChatRequest,
        authorization: str = Header(None)
):
    """
    Endpoint para chatear con GPT-4.
    Requiere autenticación via Bearer token.
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticación no proporcionado o formato inválido"
        )

    try:
        token = authorization.split("Bearer ")[1]
        user = await auth_service.get_current_user(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido o expirado"
            )

        return await chat_service.generate_chat_response(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
async def health_check():
    """
    Endpoint para verificar el estado del servicio de chat.
    No requiere autenticación.
    """
    return {"status": "ok"}