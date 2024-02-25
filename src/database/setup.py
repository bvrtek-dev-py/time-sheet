from typing import Annotated

from fastapi import Depends
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticClientSession
from motor.motor_asyncio import AsyncIOMotorClient

from time_sheet.src.settings.database import MONGO_DB_URL, MONGO_INITDB_DATABASE


def get_client() -> AgnosticClient:
    return AsyncIOMotorClient(MONGO_DB_URL)


def get_database(
    client: Annotated[AgnosticClient, Depends(get_client)]
) -> AgnosticDatabase:
    return client[MONGO_INITDB_DATABASE]


async def get_session(
    database: Annotated[AgnosticDatabase, Depends(get_database)]
) -> AgnosticClientSession:
    session = await database.client.start_session()

    try:
        yield session
    finally:
        await session.end_session()
