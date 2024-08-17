from fastapi import FastAPI
from enum import Enum


class Pokemon(str, Enum):
    bulbasaur = 1
    charmander = 2
    squirtle = 3
    pikachu = 4


app = FastAPI()

@app.get("/talk/{pokemon_id}")
async def poke_talk(pokemon_id:Pokemon):
    match pokemon_id:
        case Pokemon.bulbasaur:
            return {"pokemon_id": pokemon_id, "speech": "Bulba! Bulba-saur!"}
        case 2: #NOT REACHABLE
            return {"pokemon_id": pokemon_id, "speech": "Char! Char-man-der!"}
        case "squirtle": #NOT REACHABLE
            return {"pokemon_id": pokemon_id, "speech": "Squirtle! Squirt, squirt!"}
        case "4":
            return {"pokemon_id": pokemon_id, "speech": "Pika Pika!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int): # so that it actually returns an int
    return {"item_id": item_id}

@app.get("/items/0")
async def read_item_0():
    return {"message": "This can never be reached"}


@app.get("/read_file/{file_path:path}")
async def read_file(file_path:str):
    with open(file_path, 'r') as f:
        text = f.read()
    return {"file_text": text}