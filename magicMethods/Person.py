from Couple import Couple

class Person():
    name = ""
    years_old = 0

    def __init__(self, name, years_old) -> None:
        self.name = name
        self.years_old = years_old

    def __add__(self, person):
        couple = Couple(self,person)
        return couple