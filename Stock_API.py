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

#GET
@app.get("/stock")
def get_stock():
    return stock

#PUT
@app.put("/stock/{stock_id}")
def update_stock(stock_id:int,stocks:Stock):
    if stock_id<0 or stock_id>=len(stock):
        raise HTTPException(status_code=404,details="Stock not found")
    stock[stock_id]=stocks
    return{"mesaage":"stock updated","data":stocks}


