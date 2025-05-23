from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

with open("api/q-vercel-python.json", "r") as f:
    marks_db = json.load(f)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
async def get_marks(name: List[str] = []):
    result = [MARKS_DB.get(n, 0) for n in name]
    return JSONResponse(content={"marks": result})
