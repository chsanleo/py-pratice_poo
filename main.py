from Student import Student
from ClassRoom import ClassRoom

student1 = Student("Ethan","Zhang","dni",12)
student2 = Student("Retro","Machine","dni2",13)

classA = ClassRoom()
classA.add_student(student1)
classA.add_student(student2)

classA.show_students()