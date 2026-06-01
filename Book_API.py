from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel

app=FastAPI()

books=[]

class Book(BaseModel):
    id:int
    title:str
    author:str


#POST
