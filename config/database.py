import sqlalchemy as database
import os
from dotenv import load_dotenv
load_dotenv()


db_engine = database.create_engine(os.getenv("DATABASE_URL"), echo=True)
