from fastapi import Query, APIRouter
from src.models.user import BidangModel, HumanitiesModel, ScienceModel, TargetModel, UserModel
from typing import Optional

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    return [{"id": 1}, {"id": 2}]

@router.get("/{user_id}")
async def read_user(user_id: int):
    return {"id": user_id, "full_name": "Danny Manny", "email": "danny.manny@gmail.com"}

@router.get("/detail")
async def read_users(q: Optional[str] = Query(None, max_length=50)):
    results = {"users": [{"id": 1}, {"id": 2}]}
    if q:
        results.update({"q": q})
    return results

@router.post("/addUser")
async def add_user(user: UserModel, bidang:BidangModel):
    return {"id": user.user_id, "name": user.nama, "bidang": bidang}

@router.post("/makeTarget")
async def make_target(target: TargetModel):
    return{"university": target.UnivId, "major": target.MajorId}

@router.post("/sendScore/{bidang}}")
async def send_score(bidang: BidangModel, science:ScienceModel, humanities: HumanitiesModel):
    if bidang == BidangModel.Science:
        return{"bidang": bidang, 
                "Biology": science.Biology,
                "Chemistry": science.Chemistry,
                "Physics": science.Physics,
                "Mathematics": science.Mathematics,
                "Reading_Comprehension_Writing_Science": science.Reading_Comprehension_Writing_Science,
                "General_Reasoning_Science": science.General_Reasoning_Science,
                "Quantitative_Skills_Science": science.Quantitative_Skills_Science,
                "General_Knowledge_Understanding_Science": science.General_Knowledge_Understanding_Science
                }
    if bidang == BidangModel.Humanities:
                return{"bidang": bidang, 
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
async def read_user(user: UserModel, bidang:BidangModel):
    return {"id": user.user_id, "name": user.nama, "bidang": bidang, }

@router.delete("/{user_id}/delete")
async def read_user(user_id: int):
    return {"id": user_id, "is_deleted": True}
