from beanie import init_beanie
from pymongo import AsyncMongoClient

from crosfit_training_backend.models import DOCUMENT_MODELS


async def init_db(client: AsyncMongoClient, db_name: str) -> None:
    await init_beanie(database=client[db_name], document_models=DOCUMENT_MODELS)
