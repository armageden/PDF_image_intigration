"""
Database connection and session management
Using SQLAlchemy async with SQLite
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator
import os

from src.config import get_database_url


class Base(DeclarativeBase):
    """Base class for all database models"""
    pass


# Create async engine
engine = create_async_engine(
    get_database_url(),
    echo=False,  # Set to True for SQL debugging
    future=True
)

# Create async session factory
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def init_db():
    """Initialize database - create all tables"""
    async with engine.begin() as conn:
        # Import all models to register them
        from src.models.user import User
        from src.models.pdf_job import PDFJob
        from src.models.image import GeneratedImage
        
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency that provides database session"""
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
