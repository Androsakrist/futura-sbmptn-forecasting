from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import os
# from dotenv import load_dotenv

# DRIVER = os.getenv("POSTGRES_DRIVER")
# USERNAME = os.getenv("POSTGRES_USERNAME")
# PW = os.getenv("POSTGRES_PW")
# HOST = os.getenv("POSTGRES_HOST")
# PORT = os.getenv(5432)
# NAME = os.getenv("POSTGRES_DB")
# SQLALCHEMY_DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format(DRIVER, USERNAME, PW,HOST,PORT,NAME)

engine = create_engine('postgresql://mydb:userdata@34.128.103.193:5432/postgres')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
