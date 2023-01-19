from sqlalchemy import Column,VARCHAR,String,Text,Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentModel(Base):
    __tablename__ = "student"
    id = Column(VARCHAR(25),primary_key=True)
    name= Column(String(150))
    address = Column(Text)
    gender = Column(Enum("laki-laki","perempuan"))

