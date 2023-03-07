class Student():
    # Attributes
    name = ""
    surname = ""
    dni = ""
    years_old = 0
    score = 0

    # Methods
    def saludar (self):
        print(f"Hola, me llamo {self.name}")
    
    def birthday (self):
        self.years_old +=1

    def add_score (self, score):
        if(score >= 0 and score <= 10):
            self.score = score