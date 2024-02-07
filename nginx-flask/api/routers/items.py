from datetime import datetime

from fastapi import APIRouter, Body

from models.items import Item
from repository import db

router = APIRouter()


@router.post("/accounts/test")
def create_item(item: Item = Body(...)):
    print(item)
    return {"message": f"added: {item}"}


@router.post("/accounts/")
async def create_item(item: Item):
    doc = {
        "seq": item.seq,
        "name": item.name,
        "username": item.username,
        "email": item.email,
        "phone": item.phone,
        "timestamp": datetime.now(),
    }
    dbname = db.get_database()

    collection = dbname.get_collection("users")

    result = collection.insert_one(doc)
    return {"message": f"added: {item} {result}"}


@router.get("/accounts/")
async def get_items(skip: int = 0, limit: int = 10, q: str | None = None) -> list[Item]:
    dbname = db.get_database()
    collection = dbname.get_collection("users")
    result = collection.find().sort({"_id": 1}).skip(skip).limit(limit)

    items = [item for item in result]
    print(items)
    return items
