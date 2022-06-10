from array import array
from statistics import mean
from fastapi import Body, Query, APIRouter
from src.models.user import BidangModel, HumanitiesModel, ScienceModel, TargetModel, UserIn, UserModel, UserOut, gelModel
from typing import Optional
import pickle  

# APIRouter creates path operations for user module
router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},  
)

@router.get("/detail")
def read_users(q: Optional[str] = Query(None, max_length=50)):
    results = {"users": [{"id": 1}, {"id": 2}]}
    if q:
        results.update({"q": q})
    return results
    
@router.post("/makeTarget/")
async def send_score(science:ScienceModel, target:TargetModel):
    pickle_in = open("model_science_tree.pkl","rb")
    regressor=pickle.load(pickle_in)
    saintek = [science.Biology, science.Physics, science.Chemistry, science.Mathematics]
    rata2_saintek = mean(saintek)
    pot_saintek = [science.Reading_Comprehension_Writing_Science, 
                        science.General_Reasoning_Science, 
                        science.Quantitative_Skills_Science, 
                        science.General_Knowledge_Understanding_Science]
    mean_saintek_pot= mean(pot_saintek)
    # Biology=science['Biology']
    # Physics=science['Physics']
    # Chemistry=science['Chemistry']
    # Reading_Comprehension_Writing_Science=science['Reading Comprehension Writing Science']
    # Biology=science['Biology']
    # Biology=science['Biology']
    # Biology=science['Biology']
    # prediction = regressor.predict([[Biology, Physics, Chemistry,]])
    maketarget = regressor.predict([[
        target.MajorId, 
        science.Biology,
        science.Physics,
        science.Chemistry,
        science.Reading_Comprehension_Writing_Science,
        science.General_Reasoning_Science,
        science.Quantitative_Skills_Science,
        science.Mathematics,
        science.General_Knowledge_Understanding_Science,
        rata2_saintek,
        mean_saintek_pot,
        target.capacity,
        ]])
    output= round(maketarget[0],2)
    return{
        'hasil prediksi target kamu adalah: {}'.format(output)
    }



# @router.get("/")
# async def read_user():
#     return{"id": .user_id, "full_name": userM.nama, "email": "danny.manny@gmail.com"}

@router.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


@router.post("/addUser")
async def add_user(user: UserModel, bidang: BidangModel, gelombang: gelModel):
    return {"id": user.user_id, "name": user.nama, "bidang": bidang, "gelombang": gelombang.value}

@router.post("/sendScore/Humanities")
async def send_score(bidang: BidangModel, humanities: HumanitiesModel):
    return{
        "bidang": bidang,
        "Economy": humanities.Economy,
        "History": humanities.History,
        "Geography": humanities.Geography,
        "Sociology": humanities.Sociology,
        "Reading_Comprehension_Writing_Humanities": humanities.Reading_Comprehension_Writing_Humanities,
        "General_Reasoning_Humanities": humanities.General_Reasoning_Humanities,
        "Quantitative_Skills_Humanities": humanities.Quantitative_Skills_Humanities,
        "General_Knowledge_Understanding_Humanities": humanities.General_Knowledge_Understanding_Humanities
    }


@router.put("/updateUser")
async def add_user(user: UserModel, bidang: BidangModel, gelombang: gelModel = Body(..., description="choose gelombang")):
    return {"id": user.user_id, "name": user.nama, "bidang": bidang, "gelombang": gelombang.value}

@router.delete("/{user_id}/delete")
async def read_user(user_id: int):
    return {"id": user_id, "is_deleted": True}
