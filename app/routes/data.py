from fastapi import APIRouter
from app.schema.data import HandData
import httpx

router = APIRouter()

@router.get("/")
async def get_hand_data(link: str) -> HandData:
    game_id = link.split("/")[-1]
    poker_now_api_url = f"https://www.pokernow.club/api/games/{game_id}/log_v3"

    all_hands = []
    i = 1

    async with httpx.AsyncClient() as client:
        while True:
            print(f"Fetching hand number {i}...")
            response = await client.get(poker_now_api_url, params={"hand_number": i})
            hand_data = response.json()
            if hand_data == []:
                break
            all_hands.extend(hand_data)
            i += 1

    return HandData(data=all_hands)