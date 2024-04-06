import datetime as dt
import sys

# Se importa os.path para poder importar desde el directorio padre
from os.path import dirname, abspath
d = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(d)

from Persistance.SqlDataSource import SqlConnection
from Contracts.Interfaces.Repositories.ITaskRepository import ITaskRepository
from Contracts.Models.task import Task

class TaskRepository(ITaskRepository):
    def __init__(self, db: SqlConnection):
        self.db = db
        
    def create_task(self, task: Task) -> Task:
        query = "INSERT INTO tasks (user_id, date, time, description) VALUES (%(userId)s, %(task_date)s, %(task_time)s, %(task_description)s) RETURNING id"
        cursor = self.db.connection.cursor()
        cursor.execute(query, {'userId': task.userId, 'task_date': task.date, 'task_time': task.time, 'task_description': task.description})
        self.db.connection.commit()
        task.id = cursor.fetchone()[0]
        cursor.close()
        return task



    def get_user_tasks(self, userId: int) -> list[Task]:
        query = "SELECT * FROM tasks WHERE user_id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (userId,))
        task_parts_list = cursor.fetchall()
        user_tasks = []
        for task_list in task_parts_list:
            task = Task(task_list[3], task_list[4], task_list[2], task_list[1], task_list[0])
            user_tasks.append(task)
        cursor.close()
        return user_tasks

    def get_task(self, taskId: int) -> Task:
        query = "SELECT * FROM tasks WHERE id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (taskId,))
        task_parts = cursor.fetchone()
        task = Task(task_parts[3], task_parts[4], task_parts[2], task_parts[1], task_parts[0])
        cursor.close()
        return task

    def edit_task(self, task: Task) -> Task:

        query = "UPDATE tasks SET date = %s, time = %s, description = %s WHERE id = %s RETURNING *"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (task.date, task.time, task.description, task.id))
        self.db.connection.commit()
        task_parts = cursor.fetchone()
        task_edited = Task(task_parts[3], task_parts[4], task_parts[2], task_parts[1], task_parts[0])
        cursor.close()
        return task_edited

    def delete_task(self, taskId: int):
        query = "DELETE FROM tasks WHERE id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (taskId,))
        self.db.connection.commit()
        cursor.close()

# hacer una prueba
        
db = SqlConnection()
task_repo = TaskRepository(db)

boca = task_repo.get_task(6)
print(boca)

