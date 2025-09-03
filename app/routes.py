from fastapi import APIRouter
from .models import Item

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@router.post("/items/")
def create_item(item: Item):
    return {"message": "Item received", "item": item.dict()}

