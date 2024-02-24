from abc import ABC, abstractmethod
import sys

from os.path import dirname, abspath
d = dirname(dirname(dirname(dirname(abspath(__file__)))))
sys.path.append(d)

from Contracts.Models.task import Task

class ITaskService(ABC):
    @abstractmethod
    def create_task(self, task: Task):
        pass

    @abstractmethod
    def edit_task(self, task: Task):
        pass

    @abstractmethod
    def delete_task(self, taskId: int):
        pass

    @abstractmethod
    def get_task(self, taskId: int):
        pass