import datetime as dt
import sys
sys.path.insert(0, 'C:/Users/franc/OneDrive/Documentos/TaskManager/persitance')
from SqlDataSource import SqlConnection

class UserRepository:
    def __init__(self, db: SqlConnection):
        self.db = db

    def create_user(self, name: str, surname: str, age: int, email: str, hash_pass: str):
        # se hace la query
        query = "INSERT INTO users (name, surname, age, email, hash_pass) \
                VALUES (%(user_name)s, %(user_surname)s, %(user_age)s, %(user_email)s, %(user_hash_pass)s) \
                RETURNING *"
        
        # se crea el cursor y se ejecuta la query con los parametros
        cursor = self.db.connection.cursor()
        cursor.execute(query, {'user_name': name, 'user_surname': surname, 'user_age': age, 'user_email': email, 'user_hash_pass': hash_pass})

        # se devuelve el usuario
        user = cursor.fetchone()
        self.db.connection.commit()
        cursor.close()
        return user


    def get_user(self, userId: int):
        query = "SELECT * FROM users WHERE id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (userId,))
        user = cursor.fetchone()
        cursor.close()
        return user
    
    def edit_user(self, userId: int, name: str, surname: str, age: int, email: str, hash_pass: str):
        query = "UPDATE users SET name = %s, surname = %s, age = %s, email = %s, hash_pass = %s WHERE id = %s RETURNING *"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (name, surname, age, email, hash_pass, userId))
        user = cursor.fetchone()
        self.db.connection.commit()
        cursor.close()
        return user

    def delete_user(self, userId: int):
        query = "DELETE from users WHERE id = %s"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (userId))
        self.db.connection.commit()
        cursor.close()

# hacer una prueba
db = SqlConnection()
user_repo = UserRepository(db)
