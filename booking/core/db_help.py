from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from .config import settings


class DataBaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine: AsyncEngine = create_async_engine(url=url, echo=echo)
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )


    async def get_db(self):
        async with self.session_factory() as session:
            yield session


db_helper = DataBaseHelper(settings.db_url, echo=True)