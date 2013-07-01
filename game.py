from sign import Sign

class Game(object):
    
    PLAYER_ONE = "Player 1 wins"
    PLAYER_TWO = "Player 2 wins"
    DRAW = "It's a draw"
    
    def __init__(self, *signs):
        self.callbacks = {
  		"playerOneWins": [],
			"playerTwoWins": [],
			"nobodyWins": []
		}
        self.signs = {}
        for s in signs:
            sign = Sign(s)
            sign.draws(sign)
            self.signs[sign.name] = sign
        
    def setRules(self, callback):
        eval(callback, self.signs)
        return self
    
    def whoWins(self, firstSign, secondSign):
        if type(firstSign) is str:
            firstSign = self.signs[firstSign]
        if type(secondSign) is str:
            secondSign = self.signs[secondSign]
        if firstSign.isVictoriousWith(secondSign):
            self.execute("playerOneWins", firstSign, secondSign)
            return Game.PLAYER_ONE
        if firstSign.isBeatenBy(secondSign):
            self.execute("playerTwoWins", firstSign, secondSign)
            return Game.PLAYER_TWO
        self.execute("nobodyWins", firstSign, secondSign)
        return Game.DRAW
    
    def whenPlayerOneWins(self, callback):
        self.callbacks["playerOneWins"].append(callback)
        return self

    def whenPlayerTwoWins(self, callback):
        self.callbacks["playerTwoWins"].append(callback)
        return self
    
    def whenPlayersDraw(self, callback):
        self.callbacks["nobodyWins"].append(callback)
        return self
    
    def execute(self, callbackArray, *arguments):
        for callback in self.callbacks[callbackArray]:
            callback(*arguments)
