from fastapi import APIRouter
from src.models.user import logDB

router = APIRouter(
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    for x in logDB:
       results = "Latest prediction score :{}%".format(x)

    return results