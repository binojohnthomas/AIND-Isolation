import itertools
import random
import warnings
import time

from collections import namedtuple

from isolation import Board

from sample_players import GreedyPlayer
from sample_players import RandomPlayer
from sample_players import null_score
from sample_players import open_move_score
from sample_players import improved_score
from game_agent import CustomPlayer
from game_agent import custom_score
player_1 = CustomPlayer()

#player_2 = GreedyPlayer()
player_2 = RandomPlayer()
print(player_1,player_2)

test_game = Board(player_1, player_2)
start = time.time()
winner, moves, reason = test_game.play()
end = time.time()
#print (winner)
if reason == "timeout":
    print("Forfeit due to timeout.")
for move in moves:
    print(move)

print('Play Summary : Time taken = {0}, number of move = {1}, winner= {2}, Reason ={3}' .format(end-start, len(moves),winner,reason))