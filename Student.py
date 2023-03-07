class Student():
    # Attributes
    name = ""
    surname = ""
    dni = ""
    years_old = 0
    subject = []

    # Constructor
    def __init__ (self, name, surname, dni, years_old):
        self.name = name
        self.surname = surname
        self.dni = dni
        self.years_old = years_old

    # Methods
    def saludar (self):
        print(f"Hola, me llamo {self.name}")
    
    def birthday (self):
        self.years_old +=1

    def add_subject(self, subject):
        self.subject.append(subject)