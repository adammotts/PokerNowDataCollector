from pydantic import BaseModel
from typing import List

class HandData(BaseModel):
    hand_number: int
    data: List[str]

    class Config:
        from_attributes = True

class GameData(BaseModel):
    game_id: str
    hand_data: List[HandData]

    class Config:
        from_attributes = True

class UpdateGameDataRequest(BaseModel):
    game_id: str
    hand_data: List[HandData]
