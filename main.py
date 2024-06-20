from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as cars_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Base clear")
    await create_tables()
    print("Turn On")
    yield
    print("Turn Off")

app = FastAPI(lifespan=lifespan)
app.include_router(cars_router)




