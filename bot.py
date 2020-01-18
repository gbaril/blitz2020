from typing import Dict, List
from game_message import *
from bot_message import *
import random
from utils import *
from bfs_lib import bfs

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
        print(me.position)

        print("Dist enemy to tail: {}".format(min_dist_enemy_to_tail(game_message)))
        print("Dist me to base: {}".format(min_dist_us_to_base(game_message)))

        legal_moves = self.get_legal_moves_for_current_tick(game=game_message.game, players_by_id=players_by_id)

        target = None
        for player in game_message.players:
            if player.id != me.id:
                target = player.position

        if target:
            grille = [[game_message.game.map[i][j] for j in range(len(game_message.game.map[0]))]for i in range(len(game_message.game.map))]

            for case in me.tail:
                grille[case.y][case.x] = TileType.TAIL

            path = bfs(grille, me.position, [TileType.ASTEROIDS, TileType.BLACK_HOLE, TileType.TAIL], target)
            #  print(path)

            next_move = move_for_next_position(me.position, path[1], me.direction)
            #  print(next_move)
            return next_move

        # You can print out a pretty version of the map but be aware that
        # printing out long strings can impact your bot performance (30 ms in average).
        #print(game_message.game.pretty_map)

        return random.choice(legal_moves)

    def get_legal_moves_for_current_tick(self, game: Game, players_by_id: Dict[int, Player]) -> List[Move]:
        '''
        You should define here what moves are legal for your current position and direction
        so that your bot does not send a lethal move.

        Your bot moves are relative to its direction, if you are in the DOWN direction.
        A TURN_RIGHT move will make your bot move left in the map visualization (replay or logs)
        '''
        me: Player = players_by_id[game.player_id]

        return [move for move in Move]
