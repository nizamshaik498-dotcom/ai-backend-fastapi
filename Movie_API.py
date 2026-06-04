from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

movie=[]

class Movie(BaseModel):
    genre:str
    tickets:int

#POST
@app.post("/movie")
def create_movie(movies:Movie):
    movie.append(movies)
    return {"message":"Movie Added","data":movies}