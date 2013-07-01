from game import Game

print (Game ("rock", "paper", "scissors") \
    .setRules("scissors.beats(paper).beats(rock).beats(scissors)")
    .whoWins("rock", "paper"))
