from Student import Student
from ClassRoom import ClassRoom

"""
# Kata I y Kata II
student1 = Student("Ethan","Zhang","dni",12)
student2 = Student("Retro","Machine","dni2",13)

classA = ClassRoom()
classA.add_student(student1)
classA.add_student(student2)

classA.show_students()
"""

"""
# Kata III
studentNames = ["Ethan", "Retro", "Maria"]
subjectNames = ["Matematicas", "Lengua", "Sociales"]

classB = ClassRoom(studentNames, subjectNames)

classB.show_classInfo()
"""

# Kata IV 
studentA = Student("Manu","Sanchez", "000000000X", 20)
print(studentA.dni)
print(studentA.years_old)

studentA.years_old = 50
print(studentA.years_old)

studentA.years_old = 101
print(studentA.years_old)