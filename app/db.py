from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# This code sets up a database connection using SQLAlchemy. It creates an engine and a session factory for interacting with the database.
# The `get_db` function is a generator that provides a session to the caller and ensures that the session is closed after use.
# This is useful for dependency injection in FastAPI, allowing you to easily manage database sessions in your routes.
# The `get_db` function can be used as a dependency in FastAPI routes to provide a database session for handling requests.