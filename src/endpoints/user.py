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

# @router.get("/detail")
# def read_users(q: Optional[str] = Query(None, max_length=50)):
#     results = {"users": [{"id": 1}, {"id": 2}]}
#     if q:
#         results.update({"q": q})
#     return results

# @router.get("/detail")
# def read_users(q: Optional[str] = Query(None, max_length=50)):
#     results = {"users": [{"id": 1}, {"id": 2}]}
#     if q:
#         results.update({"q": q})
#     return results

@router.post("/makeTarget/science")
async def Science(target:TargetModel, science:ScienceModel):
    pickle_in = open("model_science_tree.pkl","rb")
    regressor=pickle.load(pickle_in)
    saintek = [science.Biology, science.Physics, science.Chemistry, science.Mathematics]
    rata2_saintek = mean(saintek)
    pot_saintek = [science.Reading_Comprehension_Writing_Science, 
                        science.General_Reasoning_Science, 
                        science.Quantitative_Skills_Science, 
                        science.General_Knowledge_Understanding_Science]
    mean_saintek_pot= mean(pot_saintek)
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
        'hasil prediksi target kamu adalah: {}%'.format(output)
    }

@router.post("/makeTarget/humanities")
async def Humanities(target:TargetModel, humanities:HumanitiesModel):
    pickle_in = open("model_humanities_tree.pkl","rb")
    regressor=pickle.load(pickle_in)
    soshum = [humanities.Economy, humanities.History, humanities.Geography, humanities.Sociology, humanities.Mathematics]
    rata2_soshum = mean(soshum)
    pot_soshum = [humanities.Reading_Comprehension_Writing_Humanities, 
                        humanities.General_Reasoning_Humanities, 
                        humanities.Quantitative_Skills_Humanities, 
                        humanities.General_Knowledge_Understanding_Humanities]
    mean_soshum_pot= mean(pot_soshum)
    maketarget = regressor.predict([[
        target.MajorId, 
        humanities.Economy,
        humanities.Geography,
        humanities.History,
        humanities.Sociology,
        humanities.Reading_Comprehension_Writing_Humanities,
        humanities.General_Reasoning_Humanities,
        humanities.Quantitative_Skills_Humanities,
        humanities.Mathematics,
        humanities.General_Knowledge_Understanding_Humanities,
        rata2_soshum,
        mean_soshum_pot,
        target.capacity,
        ]])
    output= round(maketarget[0],2)
    return{
        'hasil prediksi target kamu adalah: {}%'.format(output)
    }