from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
    tabs: list


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@router.put("/items2/{item_id}")
def update_item(item_id: int, item: Item, test: Item):
    print(type(item.tabs))
    return {"item_name": item.tabs, "item_id": item_id, "test": test}
