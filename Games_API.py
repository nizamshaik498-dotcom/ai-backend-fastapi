from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

games=[]

class Game(BaseModel):
    name:str
    genre:str
    rating:int

#POST

@app.post("/games")
def create_game(game:Game):
    games.append(game)
    return{"message":"Game Added","data":game}

#GET
@app.get("/games")
def get_games():
    return games

#PUT
@app.put("/games/{game_id}")
def update_game(game_id:int,game:Game):
    if game_id <0 or game_id>=len(games):
        raise HTTPException(status_code=404,details="Game not found")
    games[game_id]=game
    return {"message":"Game updated"}