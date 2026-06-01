from fastapi import FastAPI,HTTPSException
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