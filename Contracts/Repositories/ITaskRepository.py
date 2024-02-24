from abc import ABC, abstractmethod

class ITaskRepository(ABC):
    @abstractmethod
    def create_task(self, userId: int, task: str, date: str):
        pass

    @abstractmethod
    def get_user_tasks(self, userId: int):
        pass

    @abstractmethod
    def get_task(self, taskId: int):
        pass

    @abstractmethod
    def edit_task(self, taskId: int, task: str, date: str):
        pass

    @abstractmethod
    def delete_task(self, taskId: int):
        pass