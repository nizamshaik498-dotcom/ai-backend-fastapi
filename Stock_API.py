from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

stock=[]

class Stock(BaseModel):
    s_name:str
    price:int
    type:str



