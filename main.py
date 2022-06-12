import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI 
from routes.api import router as api_router
from db import Base, engine

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {"name": "user", "description": "This is user route"},
]

app = FastAPI()

origins = ["http://localhost:8005"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
    print("running")
