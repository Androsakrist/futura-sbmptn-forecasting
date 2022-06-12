from importlib.metadata import metadata
from typing import Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Table
from sqlalchemy.orm import relationship

user = Table('category', metadata,
                 Column('username', String, primary_key=True),
                 Column('passowrd', String(200))
                 )

class Users(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True, unique=True, nullable=False)
    password = Column(String, nullable=False)

    users = relationship("Users", back_populates="owner")

class TokenData(BaseModel):
    username: Optional[str]= None

class UserOut(BaseModel):
    username: str
    email: EmailStr

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

