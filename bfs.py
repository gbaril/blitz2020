import collections
from game_message import Point

grille = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [2,0,1,0,3],
    [0,0,1,0,0],
    [0,0,0,0,0]
]

# point: (i,j)
def neighbors(grille, point):
    i,j = point.x, point.y
    neighbors = []
    if i > 0:
        neighbors.append(Point(i-1, j))
    if j > 0:
        neighbors.append(Point(i, j-1))
    if i < len(grille) - 1:
        neighbors.append(Point(i+1, j))
    if j < len(grille[0]) - 1:
        neighbors.append(Point(i, j+1))
    return neighbors

# previous: dict[point] = point, end = point
def backtrack(previous, end):
    points = []
    points.insert(0, end)
    prev = end
    while prev != previous[prev]:
        prev = previous[prev]
        points.insert(0, prev)

    return points

# root: (i,j) obstacles: [1] target: [3]
def bfs(grille, root, obstacles, target):
    seen, previous, queue = set(), dict(), collections.deque([root])
    previous[root] = root
    while queue:
        point = queue.popleft()
        seen.add(point)
        #print(point)

        pi, pj = point.x, point.y
        if grille[pi][pj] in target:
            return backtrack(previous, point)

        for neighbor in neighbors(grille, point):
            if neighbor in seen:
                continue
            previous[neighbor] = point
            ni, nj = neighbor.x, neighbor.y
            if grille[ni][nj] in obstacles:
                continue
            else:
                queue.append(neighbor)

if __name__ == "__main__":
    print(bfs(grille, (2,0), obstacles=[1], target=[3]))
