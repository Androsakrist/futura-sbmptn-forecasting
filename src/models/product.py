# import email
import uuid as uuid_pkg
from enum import Enum, IntEnum
from pydantic import BaseModel, Field, EmailStr
from typing import Union

class UserModel(BaseModel):
    user_id: uuid_pkg.UUID = Field(
        default_factory= uuid_pkg.uuid4, nullable = False)
    # email: 
    nama: Union[str, None] = Field(
        default=None, max_length=32     
    )

class gelModel(IntEnum):
    gelombang_satu= 1
    gelombang_dua= 2

class BidangModel(Enum):
    Science = "science"
    Humanities = "humanities"

class penjurusan(BaseModel):
    Science = str
    Humanities = str

class ScienceModel(BaseModel):
    Biology: float
    Physics: float
    Chemistry: float
    Reading_Comprehension_Writing_Science: float
    General_Reasoning_Science: float
    Quantitative_Skills_Science: float
    Mathematics: float
    General_Knowledge_Understanding_Science: float
    
class HumanitiesModel(BaseModel):
    Economy: float
    History: float
    Geography: float
    Sociology: float
    Reading_Comprehension_Writing_Humanities: float
    General_Reasoning_Humanities: float
    Quantitative_Skills_Humanities: float
    Mathematics: float
    General_Knowledge_Understanding_Humanities: float


class TargetModel(BaseModel):
    MajorId: int
    capacity: int

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None
    
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None
