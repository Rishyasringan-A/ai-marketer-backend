from dotenv import load_dotenv
load_dotenv() 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, AI Marketer!"}
