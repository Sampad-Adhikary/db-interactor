from pydantic import BaseModel, EmailStr

"""
This file contains the data models for the User object.

The User object is defined as a class that inherits from pydantic's BaseModel.
The BaseModel class provides a simple way to define data models that can be
used to validate data.

The UserCreate class is used to validate the data that is sent to the server to
create a new user. It has two fields: name and email. The name field is a string
and the email field is an email address.

The UserRead class is used to return the data for a user from the database to
the client. It has three fields: id, name, and email. The id field is an integer
and the name and email fields are the same as the UserCreate class.

The class Config is used to configure the behaviour of the UserRead class.
The orm_mode parameter is set to True to tell pydantic to convert the data
from the database into a UserRead object.

The reason for using a separate class for the data model that is sent to the
client is to protect the client from changes to the internal representation of
the data. This is a best practice when designing APIs. The client should not
need to know anything about the internal implementation of the server.
"""
class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserRead(UserCreate):
    id: int

    class Config:
        model_config = {'from_attributes': True}

class UserUpdate(BaseModel):
    id: int
    name: str
    email: EmailStr
