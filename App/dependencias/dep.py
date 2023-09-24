from typing import Generator, Optional
from fastapi import Depends, FastAPI, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from .database import Session

async def get_session() -> Generator:

    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
    