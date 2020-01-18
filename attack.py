from utils import *

def attack(game_message: GameMessage):
    dist, path = min_dist_us_to_enemy(game_message)
    return None if path is None else path[1]