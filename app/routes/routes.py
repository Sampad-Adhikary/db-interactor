from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app.schemas.user import UserCreate, UserRead
from app.crud.user import create_user, get_users

router = APIRouter()

@router.post("/write", response_model=UserRead)
def write_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    This endpoint creates a new user in the database based on the UserCreate
    schema object provided in the request body.

    Args:
        user (UserCreate): The user data to create a new user record with.

    Returns:
        UserRead: The created User object with the generated ID.
    """
    return create_user(db, user)

@router.get("/read", response_model=List[UserRead])
def read_users(db: Session = Depends(get_db)):
    """
    Retrieve a list of all users from the database.

    This endpoint retrieves all user records available in the database
    and returns them as a list of UserRead schema objects.

    Args:
        db (Session): The database session used to execute the query.

    Returns:
        List[UserRead]: A list of UserRead objects representing all users
        in the database.
    """

    return get_users(db)
