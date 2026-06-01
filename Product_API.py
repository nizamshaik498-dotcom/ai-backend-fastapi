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

#PUT

@app.put("/product/{product_id}")
def update_product(product_id:int,prdct:Product):
    if product_id<0 or product_id>=len(product):
        raise HTTPException(status_code=404,details="Product notfound")
    product[product_id]=prdct
    return {"message":"Product updated"}