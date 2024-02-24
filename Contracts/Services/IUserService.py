from abc import ABC, abstractmethod
import sys

from os.path import dirname, abspath
d = dirname(dirname(dirname(dirname(abspath(__file__)))))
sys.path.append(d)

from Contracts.Models.user import User

class IUserService(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def edit_user(self, user: User):
        pass

    @abstractmethod
    def delete_user(self, userId: int):
        pass

    @abstractmethod
    def get_user(self, userId: int):
        pass

    @abstractmethod
    def get_userasks(self, userId: int):
        pass