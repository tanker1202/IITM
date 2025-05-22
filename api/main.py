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

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [marks_db.get(name, 0) for name in names]
    return JSONResponse(content={"marks": marks})
