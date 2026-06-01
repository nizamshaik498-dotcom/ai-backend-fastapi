from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

games=[]

class Games(BaseModel):
    name:str
    genre:str
    rating:int

#POST

@app.post("/games")
def create_games(game:Games):
    games.append(game)
    return{"message":"Game Added","data":game}