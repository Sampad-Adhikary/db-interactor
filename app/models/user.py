from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# This file contains the definition of the User class, which is a SQLAlchemy model. 
# This model is used to represent the structure of the "users" table in the database.

# The User class is derived from the declarative_base() function of SQLAlchemy, 
# which is a factory function that constructs a base class for declarative class definitions.

# The User class contains the definition of the columns of the "users" table, 
# which are the id, name, and email.

# The id column is an auto-incrementing integer which uniquely identifies a user. 
# The name column is a string that contains the name of the user. 
# The email column is a string that contains the email of the user. 
# The email column is also marked as unique, which means that no two users can have the same email address.

# The User class also contains the __tablename__ attribute, which specifies the name of the table in the database.
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
