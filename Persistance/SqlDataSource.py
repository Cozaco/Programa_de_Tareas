import psycopg2

try:
    connection = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        user="postgres",
        password="0802",
        database="db_task_manager"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
    cursor.close()
except Exception as ex:
    print("An error occurred:", ex)


