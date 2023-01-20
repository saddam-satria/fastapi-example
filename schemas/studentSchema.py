from pydantic import BaseModel

class StudentSchema(BaseModel):
    name: str
    address : str
    gender :str


class UpdateStudent(StudentSchema):
    name : str = None
    address : str = None 
    gender : str = None