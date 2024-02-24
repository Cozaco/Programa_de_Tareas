import sys

# Se importa os.path para poder importar desde el directorio padre
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from Contracts.Models.user import User
from Contracts.Services.IUserService import IUserService
from Persistance.Repositories.TaskRepository import TaskRepository
from Persistance.Repositories.UserRepository import UserRepository

class UserService:
    def __init__(self, userRepository: UserRepository, taskRepository: TaskRepository):
        self.userRepository = userRepository
        self.taskRepository = taskRepository

    def create_user(self, user: User):
        created_user = self.userRepository.create_user(user)
        return created_user
    
    def edit_user(self, user: User):
        edited_user = self.userRepository.edit_user(user)
        return edited_user
    
    def delete_user(self, userId: int):
        self.userRepository.delete_user(userId)

    def get_user(self, userId: int):
        user = self.userRepository.get_user(userId)
        return user

    def get_user_tasks(self, userId: int):
        tasks = self.taskRepository.get_user_tasks(userId)
        return tasks