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

#GET
@app.get("/movie")
def get_movie():
    return movie

#PUT
@app.put("/movie/{movie_id}")
def update_movie(movie_id:int,movies:Movie):
    if movie_id<0 or movie_id>=len(movie):
        raise HTTPException(status_code=404,details="Movie not found")
    movie[movie_id]= movies
    return {"message":"Movie not found","data":movies}

#DELETE
@app.delete("/movie/{movie_id}")
def delete_movie(movie_id:int):
    if movie_id<0 or movie_id>=len(movie):
        raise HTTPException(status_code=404,details="Movie not found")
    deleted_movie=movie.pop(movie_id)
    return {"message":"Movie deleted","data":deleted_movie}