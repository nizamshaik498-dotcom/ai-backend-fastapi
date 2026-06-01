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

#PUT
@app.put("/books/{book_id}")
def update_book(book_id:int,book:Book):
    if book_id<0 or book_id>=len(books):
        raise HTTPException(status_code=404,detail="Book not found")
    books[book_id]=book
    return{"message":"Book Updated","data":book}
