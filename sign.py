class Sign:
    
    def __init__(self, name):
        self.name = name
        self.signsWinsWith = []
        self.signsLosesWith = []
        self.signsDrawsWith = []

    @staticmethod
    def addToWins(self, sign):
      self.signsWinsWith.append(sign)
    
    @staticmethod
    def addToLosts(self, sign):
        self.signsLosesWith.append(sign)

    @staticmethod
    def addToDraws(self, sign):
        self.signsDrawsWith.append(sign)
        
    def fillArray(self, thisFunction, thatFunction, *args):
        for other in args:
            thisFunction(self, other)
            thatFunction(other, self)
        return other
    
    def beats(self, *signs):
        return self.fillArray(Sign.addToWins, Sign.addToLosts, *signs)
    
    def isVictoriousWith(self, that):
        return that in self.signsWinsWith
    
    def loses(self, *signs):
        return self.fillArray(Sign.addToLosts, Sign.addToWins, *signs)
    
    def isBeatenBy(self, that):
        return that in self.signsLosesWith
    
    def draws(self, *signs):
        return self.fillArray(Sign.addToDraws, Sign.addToDraws, *signs)
    
    def isADraw(self, that):
        return that in self.signsDrawsWith
        
    def __str__(self):
        return self.name
