from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

car=[]

class Car(BaseModel):
    Brand:str
    Model:str
    price:int

#POST
@app.post("/car")
def create_car(cars:Car)
    return {"message":"Car Added","data":cars}