import sys

# Se importa os.path para poder importar desde el directorio padre
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)


from fastapi import FastAPI
from Services.TaskService import TaskService
from Contracts.Models.task import Task
from DTOs.CreateDTOs.CreateTaskDTO import CreateTaskDTO
from DTOs.ResponseDTOs.Taskdto import TaskDTO
from Persistance.Repositories.TaskRepository import TaskRepository
from Persistance.SqlDataSource import SqlConnection


app = FastAPI()

# http://127.0.0.1:8000

db = SqlConnection()

task_service = TaskService(TaskRepository(db))

@app.get("/")
def root():
    return {"message": "Hello Sir, FastAPI is working!"}

@app.get("/task/{id}")
async def get_task(id: int):
    task = task_service.get_task(id)
    task_dto = TaskDTO(task.time, task.date, task.description, task.userId, task.id)

    return task_dto

@app.post("/task")
async def create_task(taskdto: CreateTaskDTO):
    task = Task(taskdto.time, taskdto.date, taskdto.description, taskdto.userId)
    created_task = task_service.create_task(task)
    task_dto = TaskDTO(created_task.time, created_task.date, created_task.description, created_task.userId, created_task.id)
    return task_dto

