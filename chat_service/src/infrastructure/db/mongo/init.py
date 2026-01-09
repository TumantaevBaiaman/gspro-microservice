from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from src.core.config import settings
from src.core.logging import logger


async def init_mongo():
    client = AsyncIOMotorClient(
        settings.MONGO_URL,
        uuidRepresentation="standard"
    )

    from src.infrastructure.db.mongo.models.chat_document import ChatDocument
    from src.infrastructure.db.mongo.models.chat_message_document import ChatMessageDocument
    from src.infrastructure.db.mongo.models.chat_participants_document import ChatParticipantDocument

    await init_beanie(
        database=client[settings.MONGO_DB_NAME],
        document_models=[
            ChatDocument,
            ChatMessageDocument,
            ChatParticipantDocument
        ],
    )
    try:
        await client.admin.command("ping")
        logger.success("MongoDB CONNECTED ✓")
    except Exception as e:
        logger.error(f"MongoDB CONNECTION ERROR: {e}")
