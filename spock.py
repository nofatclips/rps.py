from game import Game

def declareP1Winner(p1Sign, p2Sign):
    print ("Player One Wins: %s beats %s" % (p1Sign, p2Sign))

def declareP2Winner(p1Sign, p2Sign):
    print ("Player Two Wins: %s beats %s" % (p1Sign, p2Sign))
    
def callItADraw(p1Sign, p2Sign):
    print ("It's draw between %s and %s" % (p1Sign, p2Sign))

rpsls = Game ("rock", "paper", "scissors", "lizard", "spock") \
    .setRules("""
        scissors \
            .beats(paper, lizard) \
            .beats(spock, paper) \
            .beats(rock, spock) \
            .beats(scissors, rock) \
            .beats(lizard, scissors)""") \
            .whenPlayerOneWins(declareP1Winner) \
            .whenPlayerTwoWins(declareP2Winner) \
            .whenPlayersDraw(callItADraw) \

rpsls.whoWins("lizard", "spock")
