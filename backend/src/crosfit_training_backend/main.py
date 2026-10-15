from contextlib import asynccontextmanager

from fastapi import FastAPI
from pymongo import AsyncMongoClient

from crosfit_training_backend.api.routes.workouts import router as workouts_router
from crosfit_training_backend.database import init_db
from crosfit_training_backend.settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    client = AsyncMongoClient(settings.MONGO_URL, uuidRepresentation="standard")
    await init_db(client, settings.MONGO_DB_NAME)
    yield
    await client.close()


app = FastAPI(title="Crossfit Training API", lifespan=lifespan)
app.include_router(workouts_router)
