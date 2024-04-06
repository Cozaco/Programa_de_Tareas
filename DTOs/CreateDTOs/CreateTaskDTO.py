from datetime import datetime
from pydantic import BaseModel

class CreateTaskDTO(BaseModel):
    time: datetime
    date: datetime
    description: str
    userId: int
    id: int = None #TODO lo borro?