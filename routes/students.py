from fastapi import APIRouter
from models.Student import Student

studentRoute = APIRouter(prefix="/students")

@studentRoute.get("/")
async def getStudents(query : str=None):
    return {
        "message" : "studens", 
        "query" : query
    }

@studentRoute.get("/{studentID}")
async def getStudent(studentID:str):
    return studentID

@studentRoute.post("/")
async def insertStudent(student: Student):
    return student

@studentRoute.put("/{studentID}")
async def updateStudent(studentID: str, student: Student):
    return {
        "param" : studentID,
        "body" :student
    }