from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.core.config import settings


engine = create_async_engine(
    settings.ASYNC_DATABASE_URL,
    echo=False,
)

async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
