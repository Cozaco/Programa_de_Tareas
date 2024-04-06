from datetime import datetime
from pydantic import BaseModel

class TaskDTO(BaseModel):
    time: datetime
    date: datetime
    description: str
    userId: int
    id: int = None
