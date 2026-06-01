from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel

app=FastAPI()

books=[]

class Book(BaseModel):
    title:str
    author:str
    price:int


#POST
@app.post("/books")
def create_book(book:Book):
    books.append(book)
    return{"message":"Book Added","data":book}

#GET
@app.get("/books")
def get_books():
    return books