from fastapi import FastAPI
from app.routes import users

app = FastAPI(title="Simple Users API")

# Include users routes
app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI CRUD API with SQLite!"}
