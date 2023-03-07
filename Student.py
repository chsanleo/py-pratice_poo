class Student():
    # Attributes
    name = ""
    surname = ""
    dni = ""
    years_old = 0
    score = 0

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

    def add_score (self, score):
        if(score >= 0 and score <= 10):
            self.score = score



class Class():
    students = []

    def show_students(self):
        for student in self.students:
            print (student.name)

    def add_student(self, student):
        self.students.append(student)
        