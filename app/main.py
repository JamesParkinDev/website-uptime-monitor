from fastapi import FastAPI
from app.monitor import check_url, monitor

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/monitor/{user}")
def check_uptimes(user: str):
    return monitor(user)
