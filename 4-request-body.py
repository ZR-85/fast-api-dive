from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
app = FastAPI()

@app.post("/items/")
async def create_items(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.
        item_dict.update({"price_with_tax": price_with_tax})

    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}