import sys

# Se importa os.path para poder importar desde el directorio padre
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from Contracts.Models.task import Task
from Contracts.Services.ITaskService import ITaskService
from Persistance.Repositories.TaskRepository import TaskRepository
from Persistance.SqlDataSource import SqlConnection

class TaskService(ITaskService):
    def __init__(self, taskRepository: TaskRepository):
        self.taskRepository = taskRepository


    def create_task(self, task: Task):
        created_task = self.taskRepository.create_task(task)
        return created_task
    
    def edit_task(self, task: Task):
        edited_task = self.taskRepository.edit_task(task)
        return edited_task
    
    def delete_task(self, taskId: int):
        self.taskRepository.delete_task(taskId)

    def get_task(self, taskId: int):
        task = self.taskRepository.get_task(taskId)
        return task
    
# hacer una prueba
db = SqlConnection()
task_service = TaskService(TaskRepository(db))

print(task_service.get_task(6))