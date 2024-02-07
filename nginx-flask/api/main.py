# main.py
import time
from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from models.items import Item
from routers import items


api = FastAPI(title="Api")


@api.get("/hello")
def hello():
    return "Hello World!"


api.include_router(items.router)

app = FastAPI(title="Main")


@api.get("/accounts/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


app.mount("/api", api)
# moved to nginx
# app.mount("/", StaticFiles(directory="../web/dist", html=True))
