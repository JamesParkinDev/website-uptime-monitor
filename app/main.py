from fastapi import FastAPI
from app.monitor import check_url

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/check")
def check(url: str):
    return check_url(url)