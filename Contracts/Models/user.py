class user: 
    def __init__(self, id, name, surname, age, mail):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.mail = mail

    # Getter methods
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_age(self):
        return self.age
    
    def get_mail(self):
        return self.mail
    
    # Setter methods

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_age(self, age):
        self.age = age
    
    def set_mail(self, mail):
        self.mail = mail