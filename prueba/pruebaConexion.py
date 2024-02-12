import psycopg2
import datetime as dt

class SqlConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        user="postgres",
        password="0802",
        database="db_task_manager"
    )

class TaskRepository:
    def __init__(self, db: SqlConnection):
        self.db = db
        
    def create_task(self, userId: int, date: dt.date, time: dt.time, description: str):
        # solo tomar hora y minutos de la variable hour
        time = dt.time(time.hour, time.minute)

        # hacer la query
        query = "INSERT INTO tasks (user_id, date, hour, description) VALUES (%(userId)s, %(task_date)s, %(task_hour)s, %(task_description)s)"
        cursor = self.db.connection.cursor()
        cursor.execute(query, {'userId': userId, 'task_date': date, 'task_hour': time, 'task_description': description})
        self.db.connection.commit()
        cursor.close()


# prueba
        
db = SqlConnection()
task_repo = TaskRepository(db)
current_time = dt.datetime.now().time()
task_repo.create_task(1, dt.date.today(), dt.time(current_time.hour, current_time.minute), "tarea creada 3")
