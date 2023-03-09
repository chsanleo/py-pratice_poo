class User():
    name = ""
    surname = ""
    __dni = ""
    __years_old = ""

    def __init(self, name, surname, dni, years_old):
        self.name = name
        self.surname = surname
        self.__dni = dni
        self.__years_old = years_old

    @property
    def dni(self):
        return self.__dni
    
    @property
    def years_old(self):
        return self.__years_old

    @years_old.setter
    def years_old(self, years_old):
        if(years_old > 0 and years_old < 100 ):
            self.__years_old = years_old
        else:
            raise TypeError("Edad fuera de Rango")

    
    def saludar(self):
        print(f"Hola, me llamo {self.name}")
        
    def birthday(self):
        self.__years_old += 1