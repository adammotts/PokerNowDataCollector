from pydantic import BaseModel
from typing import List

class HandData(BaseModel):
    data: List

    class Config:
        from_attributes = True

class GameData(BaseModel):
    game_id: str
    hand_data: List[HandData]

    class Config:
        from_attributes = True