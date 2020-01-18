from game_message import *
from bfs_lib import bfs

def get_me(game_message: GameMessage):
    for player in game_message.players:
        if player.id == game_message.game.player_id:
            return player

def min_dist_enemy_to_tail(game_message: GameMessage):
    min_dist = 1000000
    min_path = None

    me = get_me(game_message)
    grille = game_message.game.map

    for player in game_message.players:
        if player.id != me.id:
            for case in me.tail:
                path = bfs(grille, player.position, [TileType.ASTEROIDS, TileType.BLACK_HOLE], case)
                dist = len(path)
                if dist < min_dist:
                    min_dist = dist
                    min_path = path
    return (min_dist, min_path)

def min_dist_us_to_base(game_message: GameMessage):
    me = get_me(game_message)
    grille = game_message.game.map

    for case in me.tail:
        grille[case.y][case.x] = TileType.TAIL

    our = TileType.CONQUERED.value + str(me.id)

    maxi = len(grille)
    maxj = len(grille[0])

    path = bfs(grille, me.position, [TileType.ASTEROIDS, TileType.BLACK_HOLE, TileType.TAIL], me.tail[0])
    min_dist = len(path)
    min_path = path

    for i in range(maxi):
        for j in range(maxj):
            if grille[i][j] == our:
                tous_a_nous = True
                if i > 0:
                    if grille[i-1][j] == our:
                        tous_a_nous = False
                if j > 0:
                    if grille[i][j-1] == our:
                        tous_a_nous = False
                if i < len(grille) - 1:
                    if grille[i+1][j] == our:
                        tous_a_nous = False
                if j < len(grille[0]) - 1:
                    if grille[i][j+1] == our:
                        tous_a_nous = False
                if not tous_a_nous:
                    path = bfs(grille, me.position, [TileType.ASTEROIDS, TileType.BLACK_HOLE, TileType.TAIL], Point(i, j))
                    dist = len(path)
                    if dist < min_dist:
                        min_dist = dist
                        min_path = path

    return (min_dist, min_path)
