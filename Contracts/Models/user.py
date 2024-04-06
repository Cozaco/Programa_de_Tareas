class User: 
    def __init__(self, name, surname, age, mail, hash_pass, id=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.mail = mail
        self.hash_pass = hash_pass