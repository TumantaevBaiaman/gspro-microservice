from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from src.core.config import settings
from src.core.logging import logger


async def init_mongo():
    client = AsyncIOMotorClient(
        settings.MONGO_URL,
        uuidRepresentation="standard"
    )


    await init_beanie(
        database=client[settings.MONGO_DB_NAME],
        document_models=[
        ],
    )
    try:
        await client.admin.command("ping")
        logger.success("MongoDB CONNECTED ✓")
    except Exception as e:
        logger.error(f"MongoDB CONNECTION ERROR: {e}")
