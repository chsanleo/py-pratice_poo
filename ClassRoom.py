class ClassRoom():
    students = []

    def show_students(self):
        for student in self.students:
            print (student.name)

    def add_student(self, student):
        self.students.append(student)
