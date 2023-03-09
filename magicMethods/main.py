from Person import Person

person1 = Person("Pedro",25)
person2 = Person("David",28)
person3 = Person("Jorge",22)

# Magic __add__
couple = person1 + person2
print(f"Esto es una pareja: {couple}")

family = couple + person3
print(f"Esto es una familia: {family}")