from importlib.metadata import metadata
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from typing import List, Optional
from sqlmodel import Field, SQLModel
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship, mapper
from db import Base
logDB = []

# user = Table('category', metadata,
#                  Column('username', String, primary_key=True),
#                  Column('passowrd', String(200))
#                  )

# class User(Base):
#     def __init__(self, username: str, password: str):
#         self.username = username
#         self.password = password

class User(Base):
    __tablename__ = 'user'
    username = Column(String, primary_key=True, nullable=False)
    password = Column(String, nullable=False)

class Config:
        arbitrary_types_allowed = True
        orm_mode = True

Users = sqlalchemy_to_pydantic(User)

# mapper(User, user)

class TokenData(BaseModel):
    username: Optional[str]= None

class UserCreate(BaseModel):
    username: str
    password: str

class UserInDB(UserCreate):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

class hasher:
    @staticmethod
    def get_hash_password(plain_password):
        return pwd_context.hash(plain_password)

    @staticmethod
    def verivy_password(plain_password, hash_password):
        return pwd_context.verify(plain_password, hash_password)

def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

