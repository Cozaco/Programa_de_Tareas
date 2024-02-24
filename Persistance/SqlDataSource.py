import psycopg2

class SqlConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        user="postgres",
        password="0802",
        database="db_task_manager"
    )





