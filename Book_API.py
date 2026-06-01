from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel

app=FastAPI()

books=[]

class Book(BaseModel):
    id:int
    title:str
    author:str


#POST
@app.post("/books")
def create_book(book:Book):
    books.append(book)
    return{"message":"Book Added","data":book}