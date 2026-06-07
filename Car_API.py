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
def create_car(cars:Car):
    return {"message":"Car Added","data":cars}

#GET
app.get("/car")
def get_car():
    return car

#PUT
@app.put("/car/{car_id}")
def update_car(car_id:int,cars:Car):
    if car_id<0 or car_id>=len(car):
        raise HTTPException(status_code=404,details="Car not found")
    car[car_id]=cars
    return {"message":"Car updated"}

#DELETE
@app.delete("/car/{car_id}")
def delete_car(car_id:int):
    if car_id<0 or car_id>=len(car):
        raise HTTPException(status_code=404,details="Car not found")
    deleted_car=car.pop(car_id)
    return {"message":"Car removed","data":deleted_car}