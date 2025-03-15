from typing import Union
from fastapi import FastAPI


#Define the fastapi router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

