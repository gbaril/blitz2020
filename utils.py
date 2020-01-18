from game_message import *
from bfs import bfs

def get_me(game_message: GameMessage):
    for player in game_message.players:
        if player.id == game_message.game.player_id:
            return player

def min_dist_enemy_to_tail(game_message: GameMessage):
    min_dist = 1000000

    me = get_me(game_message)
    grille = game_message.game.map
    
    for case in me.tail:
        grille[case.y][case.x] = TileType.TAIL.value

    for player in game_message.players:
        if player.id != me.id:
            print(grille)
            path = bfs(grille, player.position, [TileType.ASTEROIDS.value, TileType.BLACK_HOLE.value], [TileType.TAIL.value])
            dist = len(path)
            #print(path)
            if dist < min_dist:
                min_dist = dist

    print('fin enemy')
    return min_dist

def min_dist_us_to_base(game_message: GameMessage):
    me = get_me(game_message)
    grille = game_message.game.map

    for case in me.tail:
        grille[case.y][case.x] = TileType.TAIL.value

    end_tail = me.tail[0]
    grille[end_tail.y][end_tail.x] = TileType.END_TAIL.value

    print(grille)
    path = bfs(grille, me.position, [TileType.ASTEROIDS.value, TileType.BLACK_HOLE.value, TileType.TAIL.value], [TileType.END_TAIL.value, TileType.CONQUERED.value + str(me.id)])

    print('fin us')
    return len(path)
