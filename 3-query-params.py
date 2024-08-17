from fastapi import FastAPI

app = FastAPI()

items_db = [{"item": "mug"}, {"item": "phone"}, {"item": "table"}]

@app.get("/items/")
async def read_item(skip:int=0, limit:int=1, full:bool=False):
    if full:
        return items_db
    return items_db[skip:skip+limit]