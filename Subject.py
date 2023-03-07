class Subject():
    # Properties
    name = ""
    score = 0

    # Contructor
    def __init__(self, name):
        self.name = name

    # Methods
    def add_score (self, score):
        if(score >= 0 and score <= 10):
            self.score = score
