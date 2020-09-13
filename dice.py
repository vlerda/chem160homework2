# Homework2 2 player dice game
from random import choices
ntrials = 15000
player1wins = 0
for i in range(ntrials):
    # create player1's list, roll 3 dice, & sort highest to lowest
    player1 = []
    player1 = choices(range(1, 7), k=3)
    player1.sort(reverse = True)
    # create player2's list, roll 2 dice, test if dice equal
    player2 = []
    player2 = choices(range(1, 7), k=2)
    if player2[0] == player2[1]:
        continue
    if player2[0]+player2[1] < player1[0]+player1[1]:
        player1wins = player1wins+1
ratio = player1wins/ntrials
print(ratio)

# game is not fair because player1 wins at least 51% of the games