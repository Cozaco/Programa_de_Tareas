import datetime as dt
import sys

# Se importa os.path para poder importar desde el directorio padre
from os.path import dirname, abspath
d = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(d)

from Persistance.SqlDataSource import SqlConnection
from Contracts.Repositories.ITaskRepository import ITaskRepository
from Contracts.Models.task import Task

class TaskRepository(ITaskRepository):
    def __init__(self, db: SqlConnection):
        self.db = db
        
    def create_task(self, task: Task):
        query = "INSERT INTO tasks (user_id, date, time, description) VALUES (%(userId)s, %(task_date)s, %(task_time)s, %(task_description)s)"
        cursor = self.db.connection.cursor()
        cursor.execute(query, {'userId': task.userId, 'task_date': task.date, 'task_time': task.time, 'task_description': task.description})
        self.db.connection.commit()
        cursor.close()


    def get_user_tasks(self, userId: int):
        query = "SELECT * FROM tasks WHERE user_id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (userId,))
        task = cursor.fetchall()
        cursor.close()
        return task

    def get_task(self, taskId: int):
        query = "SELECT * FROM tasks WHERE id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (taskId,))
        task = cursor.fetchone()
        cursor.close()
        return task

    def edit_task(self, task: Task):

        query = "UPDATE tasks SET date = %s, time = %s, description = %s WHERE id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (task.date, task.time, task.description, task.id))
        self.db.connection.commit()
        cursor.close()

    def delete_task(self, taskId: int):
        query = "DELETE FROM tasks WHERE id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (taskId,))
        self.db.connection.commit()
        cursor.close()

# hacer una prueba
        
# db = SqlConnection()
# task_repo = TaskRepository(db)

#print(task_repo.get_task(6))

# task = Task(None, dt.time(12, 30), dt.date(2021, 5, 20), "esta es otra prueba", 1)

# task_repo.create_task(task)

