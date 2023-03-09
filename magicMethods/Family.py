class Family():
    relationship = []

    def add_person(sefl,person):
        sefl.relationship.append(person)
    
    def __str__(self) -> str:
        stringFamily = ""
        for person in self.relationship:
            stringFamily = stringFamily + person.name + " "

        return stringFamily 