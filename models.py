from sqlalchemy import Column,VARCHAR,String,Text,Enum
from sqlalchemy.ext.declarative import declarative_base
import uuid
Base = declarative_base()




class StudentModel(Base):
    __tablename__ = "student"
    id = Column(VARCHAR(25),primary_key=True)
    name= Column(String(150))
    address = Column(Text)
    gender = Column(Enum("laki-laki","perempuan"))

    def __init__(self,name,address,gender):
        self.name = name
        self.address = address
        self.gender = gender
        self.id = uuid.uuid4()
    
    def __repr__(self) -> str:
        return f"{self.name} {self.address} {self.gender} {self.id}"
        

