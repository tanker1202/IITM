from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
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
async def get_marks(name: list[str] = Query([])):
    result = [marks_db.get(n, 0) for n in name]
    return JSONResponse(content={"marks": result})
