import datetime as dt
import sys
sys.path.insert(0, 'C:/Users/franc/OneDrive/Documentos/TaskManager/persitance')


from SqlDataSource import SqlConnection

class TaskRepository:
    def __init__(self, db: SqlConnection):
        self.db = db
        
    def create_task(self, userId: int, date: dt.date, time: dt.time, description: str):
        time = dt.time(time.hour, time.minute) # solo tomar hora y minutos de la variable time

        query = "INSERT INTO tasks (user_id, date, time, description) VALUES (%(userId)s, %(task_date)s, %(task_time)s, %(task_description)s)"
        cursor = self.db.connection.cursor()
        cursor.execute(query, {'userId': userId, 'task_date': date, 'task_time': time, 'task_description': description})
        self.db.connection.commit()
        cursor.close()
        return task


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

    def edit_task(self, taskId: int, date: dt.date, time: dt.time, description: str):
        time = dt.time(time.hour, time.minute)

        query = "UPDATE tasks SET date = %s, time = %s, description = %s WHERE id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (date, time, description, taskId))
        self.db.connection.commit()
        cursor.close()

    def delete_task(self, taskId: int):
        query = "DELETE FROM tasks WHERE id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (taskId,))
        self.db.connection.commit()
        cursor.close()

# hacer una prueba
        
db = SqlConnection()
task_repo = TaskRepository(db)
# task_repo.create_task(1, dt.date.today(), dt.datetime.now().time(), "tarea creada 5")
task = task_repo.delete_task(4)
print(task)