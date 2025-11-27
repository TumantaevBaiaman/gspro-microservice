from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.core.config import settings


async def init_mongo():
    client = AsyncIOMotorClient(
        settings.MONGO_URL,
        uuidRepresentation="standard"
    )

    from app.domain.entities.course_entity import CourseEntity

    await init_beanie(
        database=client[settings.MONGO_DB_NAME],
        document_models=[CourseEntity],
    )

    try:
        await client.admin.command("ping")
        print("MongoDB CONNECTED ✓")
    except Exception as e:
        print("MongoDB CONNECTION ERROR:", e)
