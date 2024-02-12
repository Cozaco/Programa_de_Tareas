class Task:
    def __init__(self, date, title, description, status):
        self.date = date
        self.title = title
        self.description = description
        self.status = status

    # Getter methods
    def get_date(self):
        return self.date
    
    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    # Setter methods
    def set_date(self, date):
        self.date = date

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_status(self, status):
        self.status = status
        