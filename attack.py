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
    elif path_dor is None and path_atk is not None:
        return path_atk[1]
    elif path_dor is None and path_atk is  None:
        return None
    elif dist_atk * 1.3 < dist_dor * 1:
        return path_atk[1]
    else:
        return path_dor[1]

def run(game_message: GameMessage):
    dist_ett, path_ett = min_dist_enemy_to_tail(game_message)

    if path_ett is None:
        print("oops")
        return None

    dist_utb, path_utb = min_dist_us_to_base(game_message)

    if dist_ett <= dist_utb + 1:
        return path_utb[1]
    print("oh bou")
    print("enemy to tail : {}".format(dist_ett))
    print("us to base: {}".format(dist_utb))
    return None
