class Student():
    # Attributes
    name = ""
    surname = ""
    __dni = ""
    __years_old = 0
    subject = []

    # Constructor
    def __init__ (self, name, surname, dni, years_old):
        self.name = name
        self.surname = surname
        self.__dni = dni
        self.__years_old = years_old

    #Getters/Setters
    @property
    def dni (self):
        return self.__dni

    @property
    def years_old(self):
        return self.__years_old

    @years_old.setter
    def years_old (self, years_old):
        if(years_old > 0 and years_old < 100):
            self.__years_old = years_old
        else:
            raise TypeError("Edad fuera de rango")

    # Methods
    def saludar (self):
        print(f"Hola, me llamo {self.name}")
    
    def birthday (self):
        self.__years_old +=1

    def add_subject(self, subject):
        self.subject.append(subject)