import os 
from dotenv import load_dotenv
from numpy import var

load_dotenv(dotenv_path='.env')

class settings:
    db_projectid = os.getenv("POSTGRES_DRIVERNAME")
    db_user = os.getenv("POSTGRES_USERNAME")
    db_password = os.getenv("POSTGRES_PW")
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")
    db_name = os.getenv("POSTGRES_DB")