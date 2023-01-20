import sqlalchemy as database
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv


load_dotenv()


db_engine = database.create_engine(os.environ["DATABASE_URL"], echo=True)
session = Session(db_engine)
