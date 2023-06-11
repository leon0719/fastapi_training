from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.school


@app.get("/students")
def get_students():
    query = {}
    projection = {"name": True, "_id": False}
    students = db.students.find(query, projection)
    student_list = list(students)
    return student_list
