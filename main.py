from Student import Student
from Student import Class

student1 = Student("Ethan","Zhang","dni",12)
student2 = Student("Retro","Machine","dni2",13)

classA = Class()
classA.add_student(student1)
classA.add_student(student2)

classA.show_students()