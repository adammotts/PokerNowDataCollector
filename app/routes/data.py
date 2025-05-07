from fastapi import APIRouter
from app.schema.data import HandData
import httpx
import asyncio

router = APIRouter()

@router.get("/")

@router.post("/")
async def get_hand_data(link: str) -> HandData:
    game_id = link.split("/")[-1]
    base_url = f"https://www.pokernow.club/api/games/{game_id}/log_v3"
    
    hand_number = 1
    all_hands = []

    async with httpx.AsyncClient() as client:
        while True:
            response = await client.get(base_url, params={"hand_number": hand_number})

            if response.status_code == 429:
                print(f"Rate limited at hand {hand_number}, backing off...")
                await asyncio.sleep(2)
                continue

            if response.status_code != 200:
                raise RuntimeError(f"Request failed at hand {hand_number} with status {response.status_code}")

            try:
                hand = response.json()
            except Exception:
                print(f"Non-JSON response at hand {hand_number}: {response.text}")
                break

            if not hand:
                break

            all_hands.extend(hand)
            hand_number += 1

    return HandData(data=all_hands)
