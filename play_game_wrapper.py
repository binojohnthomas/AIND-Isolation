import itertools
import random
import warnings

from collections import namedtuple

from isolation import Board

from sample_players import RandomPlayer
from sample_players import null_score
from sample_players import open_move_score
from sample_players import improved_score
from game_agent import CustomPlayer
from game_agent import custom_score
player_1 = RandomPlayer()
player_2 = RandomPlayer()
print(player_1,player_2)
test_game = Board(player_1, player_2)
winner, moves, timeout = test_game.play()
print (winner)
if timeout == "timeout":
    print("Forfeit due to timeout.")
for move in moves:
    print(move)