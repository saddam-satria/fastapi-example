from fastapi import APIRouter,status,HTTPException
from config.database import session
from models import StudentModel
from schemas.studentSchema import StudentSchema,UpdateStudent

studentRoute = APIRouter(prefix="/students")


@studentRoute.get("/")
def getStudents(q : str=None):
    students = session.query(StudentModel).all()

    if q:
        students = getStudentByName(q)

    return  {
        "service" : {
            "name" : "student",
            "message" : "get students data"
        }, 
        "data" : students
    }

@studentRoute.post("/", status_code=status.HTTP_201_CREATED)
def postStudent(newStudent: StudentSchema):
    student = StudentModel(newStudent.name, newStudent.address, newStudent.gender)
    session.add(student)
    session.commit()
    return newStudent

@studentRoute.get("/{id}")
def getStudent(id: str):
    student = getStudentByID(id)
    return  {
    "service" : {
        "name" : "student",
        "message" : "get student data"
    }, 
    "data" : student
    }


@studentRoute.delete("/{id}")
def deleteStudent(id):
    student = getStudentByID(id)
    session.delete(student)
    session.commit()

    return  {
        "service" : {
            "name" : "student",
            "message" : "delete student data"
        }, 
        "data" : None
    }

@studentRoute.put("/{id}")
def updateStudent(id: str, updatedStudent: UpdateStudent):


    if(updatedStudent.name == ""):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="blank name")


    studentFilter = session.query(StudentModel).filter(StudentModel.id == id)
    prevStudent = studentFilter.first()
    updatedStudent = studentFilter.update({
        "name" : updatedStudent.name if updatedStudent.name else prevStudent.name ,
        "gender" : updatedStudent.gender if updatedStudent.gender else prevStudent.gender,
        "address" : updatedStudent.address if updatedStudent.address else prevStudent.address
    },synchronize_session="evaluate")
    return {
        "updated student" : id
    }


def getStudentByName(name: str):
    student = session.query(StudentModel).filter(StudentModel.name.like(f"%{name}%")).all()
    return student

def getStudentByID(id : str):
    student = session.query(StudentModel).filter(StudentModel.id == id).first()

    return student