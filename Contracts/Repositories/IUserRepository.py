from abc import ABC, abstractmethod

class IUserRepository(ABC):
    @abstractmethod
    def create_user(self, name: str, surname: str, age: int, email: str, hash_pass: str):
        pass

    @abstractmethod
    def get_user(self, userId: int):
        pass

    @abstractmethod
    def edit_user(self, userId: int, name: str, surname: str, age: int, email: str, hash_pass: str):
        pass

    @abstractmethod
    def delete_user(self, userId: int):
        pass
