from utils import *

def attack(game_message: GameMessage):
    dist, path = min_dist_us_to_enemy(game_message)
    return None if path is None else path[1]

def doritos(game_message: GameMessage):
    dist, path = min_dist_us_to_doritos(game_message)
    return None if path is None else path[1]

def attack_doritos(game_message: GameMessage):
    dist_atk, path_atk = min_dist_us_to_enemy(game_message)
    dist_dor, path_dor = min_dist_us_to_doritos(game_message)

    if path_atk is None and path_dor is not None:
        return path_dor[1]
    elif path_dor is None:
        return None
    elif dist_atk * 1.3 < dist_dor * 1:
        return path_atk[1]
    else:
        return path_dor[1]
