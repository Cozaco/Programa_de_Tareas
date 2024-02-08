class user: 
    def __init__(self, id, name, surname, age, mail):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.mail = mail

u1 = user(1, "John", "Doe", 25, "pepe@gmail.com")
print(u1.name)