import datetime as dt

class Task:
    def __init__(self, time: dt, date: dt, description, userId, id=None):
        self.id = id
        self.time = time
        self.date = date
        self.description = description
        self.userId = userId