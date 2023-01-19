from config.models import Base
from sqlalchemy import Column,VARCHAR,String,Text,Enum
from pydantic import BaseModel


class StudentModel(Base):
    __tablename__ = "student"
    id = Column(VARCHAR(25),primary_key=True)
    name= Column(String(150))
    address = Column(Text)
    gender = Column(Enum("laki-laki","perempuan"))


class StudentBody(BaseModel):
    name : str
    address : str = None
    gender : str
    