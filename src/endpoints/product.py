from src.models.user import logDB
from statistics import mean
from fastapi import APIRouter
from src.models.product import HumanitiesModel, ScienceModel, TargetModel

import pickle  
#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/products",
    tags=["Product"],
    responses={404: {"description": "Not found"}},
)

# @router.get("/detail")
# def read_users(q: Optional[str] = Query(None, max_length=50)):
#     results = {"users": [{"id": 1}, {"id": 2}]}
#     if q:
#         results.update({"q": q})
#     return results

@router.post("/createTarget/science")
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
    logDB.append(output)
    return{
        'hasil prediksi target kamu adalah: {}%'.format(output),
    }

'''
sample
{
  "target": {
    "MajorId": 9211352,
    "capacity": 24
  },
  "science": {
    "Biology": 513,
    "Physics": 413,
    "Chemistry": 336,
    "Reading_Comprehension_Writing_Science": 365,
    "General_Reasoning_Science": 389,
    "Quantitative_Skills_Science": 338,
    "Mathematics": 531,
    "General_Knowledge_Understanding_Science": 503
  }
}
'''

@router.post("/createTarget/humanities")
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
        'Chance to achieve your target: {}%'.format(output)
    }

    
'''sample
{
  "target": {
    "MajorId": 1112017,
    "capacity": 24
  },
  "humanities": {
    "Economy":700,
    "History": 700,
    "Geography": 700,
    "Sociology": 700,
    "Reading_Comprehension_Writing_Humanities": 700,
    "General_Reasoning_Humanities": 700,
    "Quantitative_Skills_Humanities": 700,
    "Mathematics": 700,
    "General_Knowledge_Understanding_Humanities": 700
  }
}
'''