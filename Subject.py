class Subject():
    # Properties
    __id = 0
    name = ""
    __score = 0

    # Contructor
    def __init__(self, name):
        self.name = name

    #Getters / Setters
    @property
    def score(self):
        return self.__score

    @property
    def id(self):
        return self.__id
    

    # Methods
    def add_score (self, score):
        if(score >= 0 and score <= 10):
            self.__score = score
