from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency function that returns a database session.

    This function is a generator that provides a session to the caller and ensures that the session is closed after use.
    It is useful for dependency injection in FastAPI, allowing you to easily manage database sessions in your routes.

    Yields:
        Session: A database session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()