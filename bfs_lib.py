from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game_message import Point


grid = [
    [1,1,1,1,1],
    [1,1,-1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
]

def bfs(matrix, start, obstacles, target):
    new_matrix = []
    for i, row in enumerate(matrix):
        new_matrix.append([])
        for j, col in enumerate(row):
            if matrix[i][j] in obstacles:
                new_matrix[i].append(-1)
            else:
                new_matrix[i].append(1)

    grid = Grid(matrix=new_matrix)

    start = grid.node(start.x, start.y)
    end = grid.node(target.x, target.y)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    #  print('operations:', runs, 'path length:', len(path))
    #  print(grid.grid_str(path=path, start=start, end=end))

    return list(map(lambda p: Point(p[0], p[1]), path))


if __name__ == '__main__':
    grid = Grid(matrix=grid)

    start = grid.node(0, 0)
    end = grid.node(2, 2)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))

    print(path)
