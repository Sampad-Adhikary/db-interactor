from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

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
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

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
    return db.query(User).all()
