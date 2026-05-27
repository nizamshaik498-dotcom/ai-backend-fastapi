from turtle import st
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Server is running! Visit/docs for API documentation."}

@app.get("/home")
def home():
    return {"message": "FastAPI working!"}
@app.get("/msg")
def msg():
    return {"message": "Home Page!"}
@app.get("/user")
def user():
    return {"name":"S.Mohammed Nijamuddin","role":"AI backend engineer"}

#POST request

@app.post("/create-user")
def create_user():
    return {"message":"user created successfully"}

#PUT request

@app.put("/update-user")
def update_user():
    return {"message":"user updated successfully"}


#DELETE request

@app.delete("/delete-user")
def delete_user():
    return {"message":"user deleted successfully"}

#path parameters

@app.get("/student/{student_id}")
def get_student(student_id: int):
    return {"student_id":student_id,"message":"Student data fetched successfully"}

@app.get("/student1/{student1_name}")
def get_student1(student1_name: str):
    return {"student1_name":student1_name,"message":"fetched student name"}

#Query parameters

@app.get("/search")
def search(name: str,age: int):
    return {"student_name":name,"student_age":age}

#Request body

class Student(BaseModel):
    name:str
    age:int
    course:str
@app.post("/student")
def create_student(student:Student):
    return{"message":"student created","data":student}

#Request body

class Employee(BaseModel):
    name:str
    emp_id:int
    dept:str
@app.post("/employee")
def create_employee(employee:Employee):
    return {"message":"Employee Data","data":employee}

employees=[]
class Employee(BaseModel):
    name:str
    e_id:int
    dept:str
@app.post("/employee")
def create_employee(employee:Employee):
    employee.append(Employee)
    return {"message":"Employee added data","data":employee}
@app.get("/employees")
def get_employees():
    return {"message":"Employee List","data":employees}