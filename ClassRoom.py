from Student import Student
from Subject import Subject

class ClassRoom():
    
    teacher = None # Empty object
    students = []
    subjects = []

    def __init__(self, studentsNames, subjectsNames) -> None:
        self.add_studentsNameList(studentsNames)
        self.add_subjectsNameList(subjectsNames)


    def add_subject(self, subject) -> None:
        self.subjects.append(subject)

    def add_subjectsNameList(self, subjectsNames):
        for name in subjectsNames:
            new_subject = Subject(name)
            self.add_subject(new_subject)

    def del_subject(self, subject) -> None:
        self.subjects.remove(subject)


    def add_student(self, student) -> None:
        if (student.years_old >= 18):
            self.students.append(student)

    def add_studentsNameList(self, studentsNames):
        for name in studentsNames:
            new_student = Student(name, "", "", 18)
            self.add_student(new_student)

    def del_student(self, student) -> None:
        self.students.remove(student)


    def show_students(self):
        print("Estudiantes: ")
        for student in self.students:
            print(f" - {student.name}")

    def show_subjects(self):
        print("Asignaturas")
        for subject in self.subjects:
            print (f" - {subject.name}")

    def show_classInfo(self):
        self.show_students()
        self.show_subjects()