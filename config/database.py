import sqlalchemy as database
import os
from dotenv import load_dotenv
from sqlalchemy import MetaData


load_dotenv()

DB_CONF = {
    "DB_HOST" : os.getenv("DB_HOST"), 
    "DB_USERNAME" : os.getenv("DB_USERNAME"), 
    "DB_PASSWORD" : os.getenv("DB_PASSWORD"), 
    "DB_DATABASE" : os.getenv("DB_DATABASE"), 
}


db_engine = database.create_engine(f"mysql+pymysql://{DB_CONF['DB_USERNAME']}:{DB_CONF['DB_PASSWORD']}@{DB_CONF['DB_HOST']}/{DB_CONF['DB_DATABASE']}", echo=True)
metadata = MetaData()