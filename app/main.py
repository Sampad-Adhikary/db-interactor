from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.models.user import Base
from app.db import engine
from app.routes import routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run on startup
    """
    Lifespan context manager for FastAPI application.

    This context manager is used as the lifespan parameter for FastAPI.
    It is executed on application startup and shutdown.

    On startup, it creates all tables in the database if they do not exist.
    On shutdown, it does nothing for now, but can be used to close resources,
    flush logs, etc.
    """
    Base.metadata.create_all(bind=engine)

    yield  # This point transfers control to the application

    # Run on shutdown (if needed)
    # e.g., close resources, flush logs etc.

app = FastAPI(lifespan=lifespan)

app.include_router(routes.router)
