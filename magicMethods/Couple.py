from Family import Family

class Couple():
    relationship = []

    def __init__(self, person1, person2) -> None:
        self.relationship.append(person1)
        self.relationship.append(person2)

    def __str__(self):
        couple =""
        for person in self.relationship:
            couple = couple + person.name + " "
        return couple
    
    def __add__(self, newPerson):
        family = Family()
        family.add_person(newPerson)
        for person in self.relationship:
            family.add_person(person)
        return family