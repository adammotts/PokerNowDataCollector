from fastapi import APIRouter, Body
from app.schema.game_data import GameData, HandData, UpdateGameDataRequest
from app.models.game_data import game_data_model
import httpx
import asyncio

router = APIRouter()

@router.post("")
async def bulk_record_hand_data(game_data: UpdateGameDataRequest = Body(...)):
    await game_data_model.create_game_data(game_id=game_data.game_id, hand_data=[hand.model_dump() for hand in game_data.hand_data])

@router.get("")
async def get_game_data(pokernow_url: str) -> GameData:
    game_id = pokernow_url.split("/")[-1]
    base_url = f"https://www.pokernow.club/api/games/{game_id}/log_v3"
    
    hand_number = 1
    all_hands = []

    async with httpx.AsyncClient() as client:
        while True:
            response = await client.get(base_url, params={"hand_number": hand_number})

            if response.status_code == 429:
                print(f"Rate limited at hand {hand_number}, backing off...")
                await asyncio.sleep(4)
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

            all_hands.append(HandData(hand_number=hand_number, data=[message["msg"] for message in hand]))
            hand_number += 1

    await game_data_model.create_game_data(game_id=game_id, hand_data=[hand.model_dump() for hand in all_hands])
    return GameData(game_id=game_id, hand_data=all_hands)
