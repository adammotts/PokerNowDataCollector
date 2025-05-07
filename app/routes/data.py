from fastapi import APIRouter
from app.schema.data import HandData

router = APIRouter()

@router.post("/")
async def get_hand_data(link: str) -> HandData:
    return None