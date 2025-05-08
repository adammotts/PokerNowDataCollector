from datetime import datetime
from typing import List
from motor.motor_asyncio import AsyncIOMotorCollection
from app.schema.game_data import GameData
from app.database.mongodb import db

class GameDataModel:
    def __init__(self):
        self.collection: AsyncIOMotorCollection = db["game_data"]
        
    async def create_game_data(self, game_id: str, hand_data: List[dict]) -> None:
        game = await self.collection.find_one({"game_id": game_id})

        if game:
            updated_hand_data = game.get("hand_data", []) + hand_data
            await self.collection.update_one(
                {"_id": game["_id"]},
                {"$set": {"hand_data": updated_hand_data}}
            )

        else:
            new_game = {
                "game_id": game_id,
                "hand_data": hand_data,
                "created_at": datetime.now()
            }
            await self.collection.insert_one(new_game)

    async def get_all_game_data(self) -> List[GameData]:
        game_data_list = await self.collection.find({}).to_list(length=None)
       
        return [GameData(**game) for game in game_data_list]

    async def delete_all_bathrooms(self) -> None:
        await self.collection.delete_many({})

game_data_model = GameDataModel()