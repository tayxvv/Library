from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from .config import setting

engine: AsyncEngine = create_async_engine(setting.DB_URL)

Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine 
)
