class Task:
    def __init__(self, date, name, description, status):
        self.date = date
        self.name = name
        self.description = description
        self.status = status

    # Getter methods
    def get_date(self):
        return self.date
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    # Setter methods
    def set_date(self, date):
        self._date = date

    def set_name(self, name):
        self._name = name

    def set_description(self, description):
        self._description = description

    def set_status(self, status):
        self._status = status
        