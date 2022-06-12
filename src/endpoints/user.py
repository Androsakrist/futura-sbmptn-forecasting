from fastapi import APIRouter, Depends, HTTPException, status
from src import models
from db import get_db
from sqlalchemy.orm import Session
from src.models.user import User, Users, UserCreate, logDB, hash, verify, Token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter(
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/")
async def read_root():
    return {"hello user, dont forget to login to see your latest prediction"}

@router.post("/createUser", status_code=status.HTTP_201_CREATED, response_model=UserCreate)
def create_user(user: Users, db: Session = Depends(get_db)):
    # hash the password
    hashed_password = hash(user.password)
    Users.password = hashed_password
    new_user = Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)
    return new_user

@router.post('/auth', response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # username =
    # password =
    user = db.query(User).filter(
        User == user_credentials.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")


# authentication user token
@router.post("/token", tags=["login"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # print(form_data)
    return{"access token": form_data.username + 'token'}

# give permission if logged in
@router.post("/predictions")
async def read_root(token: str = Depends(oauth2_scheme)):
    # print (token)
    for x in logDB:
       results = "Latest prediction score :{}%".format(x)

    return results
    