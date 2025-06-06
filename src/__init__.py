from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.books.routes import books_router

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Starting up the Server !!!!!!!!!!...")
    await init_db()
    yield
    print("Shutting down !!!!!!!!!!!!...")
   

app = FastAPI(
    title="Books API",
    description="A simple API for managing books",
    version="0.1.0",
    contact={
        "name": "Astonie Mukiwa",
        "email": "amukiwa@mitra.mw",
    },
    license_info={"name": "MIT"},
    lifespan=life_span,
)

version = "v1"
app.include_router(books_router, prefix=f"/api/{version}/books", tags=["books"])
