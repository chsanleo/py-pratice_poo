from Animal import Animal
from Pet import Pet

class Dog(Animal, Pet):

    def __init__(self, name, owner, height, weight) -> None:
        Animal.__init__(self, "Perro", height, weight)
        Pet.__init__(self, name, owner)