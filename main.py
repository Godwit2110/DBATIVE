from fastapi import FastAPI
from .Persistence.database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
async def health():
    return {"status": "ok"}