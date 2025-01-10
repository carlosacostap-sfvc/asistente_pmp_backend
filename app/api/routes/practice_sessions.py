from fastapi import APIRouter, HTTPException
from app.models.practice_session import PracticeSession, PracticeSessionCreate
from app.services.supabase_service import supabase_service

router = APIRouter()

@router.post("/practice-sessions", response_model=PracticeSession)
async def create_practice_session(session: PracticeSessionCreate):
    try:
        return await supabase_service.create_practice_session(session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/practice-sessions/{session_id}", response_model=PracticeSession)
async def get_practice_session(session_id: int):
    try:
        return await supabase_service.get_practice_session(session_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))