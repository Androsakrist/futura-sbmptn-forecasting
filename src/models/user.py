from dataclasses import field
import email
import uuid as uuid_pkg


from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Union



class UserModel(BaseModel):
    user_id: uuid_pkg.UUID = field(
        default_factory= uuid_pkg.uuid4, nullable = False)
    # email: 
    nama: Union[str, None] = Field(
        default=None, max_length=32
    )    
    gelombang: list[int] = 1


class BidangModel(Enum):
    Science = "science"
    Humanities = "humanities"

class penjurusan(BaseModel):
    Science = str
    Humanities = str


class ScienceModel(BaseModel):
    Biology: int
    Chemistry: int
    Physics: int
    Mathematics: int
    Reading_Comprehension_Writing_Science: int
    General_Reasoning_Science: int
    Quantitative_Skills_Science: int
    General_Knowledge_Understanding_Science: int


class HumanitiesModel(BaseModel):
    bidang = BidangModel.Humanities
    Economy: int
    History: int
    Geography: int
    Sociology: int
    Reading_Comprehension_Writing_Humanities: int
    General_Reasoning_Humanities: int
    Quantitative_Skills_Humanities: int
    General_Knowledge_Understanding_Humanities: int


class TargetModel(BaseModel):
    MajorId: int
    UnivId: int
