from fastapi import APIRouter
from app.schema.item import Item

router = APIRouter()

@router.post("/")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
