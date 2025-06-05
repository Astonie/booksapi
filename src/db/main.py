from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

engine =  AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL, 
        echo=True
))


async def init_db():
    async with engine.begin() as conn:
        statement  = text("select 'hello';")
        result = await conn.execute(statement)
        print(result.all())
        


async def close_db():
    await engine.dispose()

