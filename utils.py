from game_message import *
from bfs_lib import bfs

def get_me(game_message: GameMessage):
    for player in game_message.players:
        if player.id == game_message.game.player_id:
            return player

def min_dist_enemy_to_tail(game_message: GameMessage):
    min_dist = 1000000

    me = get_me(game_message)
    #  grille = [[game_message.game.map[i][j] for j in range(len(game_message.game.map[0]))]for i in range(len(game_message.game.map))]
    grille = game_message.game.map

    for player in game_message.players:
        if player.id != me.id:
            for case in me.tail:
                path = bfs(grille, player.position, [TileType.ASTEROIDS, TileType.BLACK_HOLE], case)
                dist = len(path)
                print(path)
                if dist < min_dist:
                    min_dist = dist

    return min_dist

def min_dist_us_to_base(game_message: GameMessage):
    me = get_me(game_message)
    grille = [[game_message.game.map[i][j] for j in range(len(game_message.game.map[0]))]for i in range(len(game_message.game.map))]

    for case in me.tail:
        grille[case.y][case.x] = TileType.TAIL

    end_tail = me.tail[0]
    grille[end_tail.y][end_tail.x] = TileType.END_TAIL

    path = bfs(grille, me.position, [TileType.ASTEROIDS, TileType.BLACK_HOLE, TileType.TAIL], [TileType.END_TAIL, str(TileType.CONQUERED) + str(me.id)])
    return len(path)
