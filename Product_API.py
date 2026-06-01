from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

product=[]

class Product(BaseModel):
    name:str
    price:int
    brand:str

#POST

@app.post("/product")
def create_product(prdct:Product):
    product.append(prdct)
    return{"message":"product added","data":prdct}

#Get

@app.get("/product")
def get_product():
    return product