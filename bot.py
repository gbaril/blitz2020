from typing import Dict, List
from game_message import *
from bot_message import *
import random


class Bot:

    def __init__(self):
        '''
        This method should be use to initialize some variables you will need throughout the game.
        '''
        self.index = 0
        self.lastPosition = Point(-10, -10) #offset out of bounds

    def diedLastTick(self, me, game):
        return abs(self.lastPosition.x - me.position.x) + abs(self.lastPosition.y - me.position.y) != 1

    def getNextMove(self):

        square = [Move.FORWARD, Move.FORWARD, Move.TURN_LEFT, Move.FORWARD, Move.TURN_LEFT, Move.FORWARD, Move.FORWARD]
        moveForward2 = [Move.FORWARD, Move.FORWARD]
        sequence = square * 2 + moveForward2 + square + [Move.TURN_RIGHT] + square[1:] + moveForward2 + square + [Move.TURN_RIGHT] + moveForward2

        self.index += 1
        return sequence[self.index % len(sequence)]



    def get_next_move(self, game_message: GameMessage) -> Move:
        '''
        Here is where the magic happens, for now the moves are random. I bet you can do better ;)
        '''
        players_by_id: Dict[int, Player] = game_message.generate_players_by_id_dict()

        me = players_by_id[game_message.game.player_id]
        if (self.diedLastTick(me, game_message.game)):
            self.index = 0

        self.lastPosition = me.position

        legal_moves = self.get_legal_moves_for_current_tick(game=game_message.game, players_by_id=players_by_id)

        return self.getNextMove()


        # You can print out a pretty version of the map but be aware that
        # printing out long strings can impact your bot performance (30 ms in average).
        # print(game_message.game.pretty_map)

        #return random.choice(legal_moves)

    def get_legal_moves_for_current_tick(self, game: Game, players_by_id: Dict[int, Player]) -> List[Move]:
        '''
        You should define here what moves are legal for your current position and direction
        so that your bot does not send a lethal move.

        Your bot moves are relative to its direction, if you are in the DOWN direction.
        A TURN_RIGHT move will make your bot move left in the map visualization (replay or logs)
        '''
        me: Player = players_by_id[game.player_id]

        return [move for move in Move]


