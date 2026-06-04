from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

stock=[]

class Stock(BaseModel):
    s_name:str
    price:int
    type:str

#POST
@app.post("/stock")
def create_stock(stocks:Stock):
    stock.append(stocks)
    return {"message":"Stock Added","data":stocks}


