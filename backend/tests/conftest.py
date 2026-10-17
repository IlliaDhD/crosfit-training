import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from pymongo import AsyncMongoClient

from crosfit_training_backend.database import init_db
from crosfit_training_backend.main import app
from crosfit_training_backend.settings import get_settings

TEST_DB = "crossfit_test"


@pytest_asyncio.fixture
async def client():
    mongo = AsyncMongoClient(get_settings().MONGO_URL, uuidRepresentation="standard")
    await init_db(mongo, TEST_DB)
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as c:
        yield c
    await mongo.drop_database(TEST_DB)
    await mongo.close()
