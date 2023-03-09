class Animal():
    species = ""
    height = 0
    weight = 0

    def __init__(self, species, height, weight) -> None:
        self.species = species
        self.height = height
        self.weight = weight
    
    def eat(self):
        print("Estoy comiendo")
    
    def hunt(self):
        print("Estoy cazando")

    def sleep(self):
        print("Zzzzzzz")