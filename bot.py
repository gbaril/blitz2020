from typing import Dict, List
from game_message import *
from bot_message import *
import random
from utils import *
from bfs_lib import bfs
from attack import *

def move_for_next_position(start, dest, direction):
    delta = (dest.x - start.x, dest.y - start.y)

    if direction == Direction.LEFT and delta == (-1, 0):
        return Move.FORWARD
    elif direction == Direction.LEFT and delta == (0, 1):
        return Move.TURN_LEFT
    elif direction == Direction.LEFT and delta == (0, -1):
        return Move.TURN_RIGHT

    elif direction == Direction.RIGHT and delta == (1, 0):
        return Move.FORWARD
    elif direction == Direction.RIGHT and delta == (0, 1):
        return Move.TURN_RIGHT
    elif direction == Direction.RIGHT and delta == (0, -1):
        return Move.TURN_LEFT

    elif direction == Direction.UP and delta == (0, -1):
        return Move.FORWARD
    elif direction == Direction.UP and delta == (-1, 0):
        return Move.TURN_LEFT
    elif direction == Direction.UP and delta == (1, 0):
        return Move.TURN_RIGHT

    elif direction == Direction.DOWN and delta == (0, 1):
        return Move.FORWARD
    elif direction == Direction.DOWN and delta == (-1, 0):
        return Move.TURN_RIGHT
    elif direction == Direction.DOWN and delta == (1, 0):
        return Move.TURN_LEFT

class Bot:

    def __init__(self):
        '''
        This method should be use to initialize some variables you will need throughout the game.
        '''

    def get_next_move(self, game_message: GameMessage) -> Move:
        '''
        Here is where the magic happens, for now the moves are random. I bet you can do better ;)
        '''
        players_by_id: Dict[int, Player] = game_message.generate_players_by_id_dict()
        me = get_me(game_message)

        # rewrite the map :3
        for case in me.tail:
            game_message.game.map[case.y][case.x] = TileType.OUR_TAIL.value
        game_message.game.map[me.tail[0].y][me.tail[0].x] = TileType.END_TAIL.value

        direction = run(game_message)
        if direction is None: #SI ON NE RUN PAS
            direction = attack_doritos(game_message)
            if direction is None: #SI PAS DE DORITOS, ENNEMY, RANDOM
                print("RANDOM")
                legal_moves = self.get_legal_moves_for_current_tick(game=game_message.game, players_by_id=players_by_id)
                direction = random.choice(legal_moves)
            else:
                print("ATTACK")
                direction = move_for_next_position(me.position, direction, me.direction)
        else:
            print("RUN")
            direction = move_for_next_position(me.position, direction, me.direction)

        return direction

    def get_legal_moves_for_current_tick(self, game: Game, players_by_id: Dict[int, Player]) -> List[Move]:
        '''
        You should define here what moves are legal for your current position and direction
        so that your bot does not send a lethal move.

        Your bot moves are relative to its direction, if you are in the DOWN direction.
        A TURN_RIGHT move will make your bot move left in the map visualization (replay or logs)
        '''
        me: Player = players_by_id[game.player_id]

        return [move for move in Move]
