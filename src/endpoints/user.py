from fastapi import APIRouter, Depends
from src.models.user import logDB
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter(
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/")
async def read_root():
    return {"hello user, dont forget to login to see your latest prediction"}

# authentication user token
@router.post("/token", tags=["login"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # print(form_data)
    return{"access token": form_data, "token type": "bearer"}

# give permission if logged in
@router.get("/predictions")
async def read_root(token: str = Depends(oauth2_scheme)):
    # print (token)
    for x in logDB:
       results = "Latest prediction score :{}%".format(x)

    return results
    