from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException, status
import json

def create_user(db: Session, user: UserCreate):
    """
    Create a new user in the database.

    This function takes a database session and a UserCreate schema object
    as inputs. It creates a new User model instance with the provided
    name and email, adds it to the database session, commits the transaction,
    and refreshes the instance to retrieve the generated ID.

    Args:
        db (Session): The database session to use for the transaction.
        user (UserCreate): The user data used to create a new user record.

    Returns:
        User: The created User object with the generated ID.
    """

    db_user = User(name=user.name, email=user.email)
    # print(repr(db_user), flush=True)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        # convert pydantic model to dict and json
        # user_dict = user.model_dump()
        # user_data = user.model_dump_json()

        user_id = db_user.get_uid()

        return JSONResponse(
            content={"message": "User created successfully", "id": user_id},
            status_code=status.HTTP_201_CREATED,
        )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists.",
        )
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}",
        )

def get_users(db: Session):
    
    """
    Retrieve a list of all users from the database.

    This function takes a database session and returns a list of all User
    objects in the database.

    Args:
        db (Session): The database session to use for the query.

    Returns:
        List[User]: A list of all User objects in the database.
    """
    try:
        query_results = db.query(User).all()
        users = [UserRead(id=user.id, name=user.name, email=user.email).model_dump() for user in query_results]
        # print(type(query_results), flush=True)
        return JSONResponse(
            content={"message": "Users retrieved successfully", "users": users},
            status_code=status.HTTP_200_OK,
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}",
        )

def get_user_by_id(db: Session, user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        user_data = UserRead(id=user.id, name=user.name, email=user.email).model_dump()
        return JSONResponse(
            content={"message": "User retrieved successfully", "user": user_data},
            status_code=status.HTTP_200_OK,
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Database error: {str(e)}",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An unexpected error occurred: {str(e)}",
        )

def update_user_db(db: Session, user: UserUpdate):
    try:
        db_user = db.query(User).filter(User.id == user.id).first()
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        db_user.name = user.name
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
        return JSONResponse(
            content={"message": "User updated successfully", "user": user.model_dump()},
            status_code=status.HTTP_200_OK,
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: {str(e)}",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: {str(e)}",
        )