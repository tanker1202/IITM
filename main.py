from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

with open("q-vercel-python.json", "r") as f:
    marks_db = json.load(f)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "Hello, World!"}

@app.get("/api")
async def get_marks(name: List[str] = Query(default=[])):
    result = [
        marks_db["marks"] if marks_db["name"] == n else 0
        for n in name
    ]
    return JSONResponse(content={"marks": result})
