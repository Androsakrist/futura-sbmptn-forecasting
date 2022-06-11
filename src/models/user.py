from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True, unique=True, nullable=False)
    password = Column(String, nullable=False)

    users = relationship("Users", back_populates="owner")


class UserOut(BaseModel):
    username: str
    email: EmailStr

logDB = []

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

class hasher:
    @staticmethod
    def get_hash_password(plain_password):
        return pwd_context.hash(plain_password)

    @staticmethod
    def verivy_password(plain_password, hash_password):
        return pwd_context.verify(plain_password, hash_password)