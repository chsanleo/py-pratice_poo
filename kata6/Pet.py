class Pet():
    name = ""
    owner = ""
    
    def __init__(self, name, owner) -> None:
        self.name = name
        self.owner = owner
    
    def sit (self):
        print("Estoy sentado")

    def give_hand(self):
        print("Doy la pata")