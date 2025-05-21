from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

with open("q-vercel-python.json", "r") as f:
    marks_db = json.load(f)

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [marks_db.get(name, 0) for name in names]
    return JSONResponse(content={"marks": marks})

# For Vercel deployment, add this handler
# vercel.json should route /api to this file's app
