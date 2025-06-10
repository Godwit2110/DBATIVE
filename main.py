import logging
from fastapi import FastAPI
from Persistence.database import init_db
from Routes.UsedProduct_route import router as usedproduct_router
from Routes.User_route import router as user_router
from Routes.Category_route import router as category_router
from Routes.Transaction_route import router as transaction_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Starting application")

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/version")
async def version():
    return {"version": "1.0.0"}

# Register all routers
app.include_router(usedproduct_router)
app.include_router(user_router)
app.include_router(category_router)
app.include_router(transaction_router)