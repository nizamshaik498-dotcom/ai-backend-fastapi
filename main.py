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
