from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # للتجربة فقط، يسمح لأي واجهة HTML بالاتصال
    allow_methods=["*"],      # يسمح بكل أنواع الطلبات GET, POST...
    allow_headers=["*"],      # يسمح بكل الـ headers
)

class Student(BaseModel):
    id: int
    name: str
    grade: int

students = [
    Student(id=1, name="issa", grade=5),
    Student(id=2, name="sara", grade=6),
]

@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_student(new_student: Student):
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student deleted"}
    return {"error": "Student not found"}