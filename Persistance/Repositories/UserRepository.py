import datetime as dt
import sys

# Se importa os.path para poder importar desde el directorio padre
from os.path import dirname, abspath
d = dirname((dirname(dirname(abspath(__file__)))))
sys.path.append(d)

from Persistance.SqlDataSource import SqlConnection
from Contracts.Repositories.IUserRepository import IUserRepository
from Contracts.Models.user import User

class UserRepository(IUserRepository):
    def __init__(self, db: SqlConnection):
        self.db = db

    def create_user(self, user: User):
        # se hace la query
        query = "INSERT INTO users (name, surname, age, mail, hash_pass) \
                VALUES (%(user_name)s, %(user_surname)s, %(user_age)s, %(user_email)s, %(user_hash_pass)s) \
                RETURNING *"
        
        # se crea el cursor y se ejecuta la query con los parametros
        cursor = self.db.connection.cursor()
        cursor.execute(query, {'user_name': user.name, 'user_surname': user.surname, 'user_age': user.age, 'user_email': user.mail, 'user_hash_pass': user.hash_pass})

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
    
    def edit_user(self, user: User):
        query = "UPDATE users SET name = %s, surname = %s, age = %s, mail = %s, hash_pass = %s WHERE id = %s RETURNING *"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (user.name, user.surname, user.age, user.mail, user.hash_pass, user.id))
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

# db = SqlConnection()
# user_repo = UserRepository(db)


# print(user_repo.get_user(6))

# user = User(id=None, name="Juan", surname="Perez", age=25, mail="juanperez@mail.com", hash_pass="1234")

# user_repo.create_user(user)