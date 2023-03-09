from User import User

class Student(User):

    subjects = []

    def __init__ (self, name, surname, dni, years_old):
        super().__ini__(name, surname, dni, years_old)

    def add_subject(self, subject):
        self.subject.append(subject)