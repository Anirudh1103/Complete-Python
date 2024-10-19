# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random as gamescore

def game():
    score = gamescore.randint(0,100)
    return score
new_score = str(game())
print(new_score)
# The game() function returns a random score between 0 and 100.
with open("hi-score.txt","r") as Rfile:
    old_score = Rfile.read()
    if old_score < new_score:
        with open("hi-score.txt","w") as Wfile:
            Wfile.write(str(new_score))
