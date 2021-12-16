import sys

def traversal(grid):
    costs = {(0, 0): 0}
    limit = len(grid)
    points = [[0, 0]]
    for point in points:
        x, y = point[0], point[1]
        neighbors = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
        for neighbor in neighbors:
            x_n, y_n = neighbor[0], neighbor[1]
            if not (0 <= x_n < limit) or not (0 <= y_n < limit): continue
            if (x_n, y_n) in costs and costs[x_n, y_n] <= costs[x, y] + grid[x_n][y_n]: continue
            costs[x_n, y_n] = costs[x, y] + grid[x_n][y_n]
            points.append(neighbor)

    return costs[limit - 1, limit - 1]


def partOne():
    with open(sys.argv[1]) as f:
        grid = [[int(n) for n in line.strip()] for line in f if line.strip()]
    return traversal(grid)

def partTwo():
    with open(sys.argv[1]) as f:
        grid = [[int(n) for n in line.strip()] for line in f if line.strip()]
    limit = len(grid)
    new_grid = []
    for i in range(5*limit):
        new_grid.append([])
        for j in range(5*limit):
            new_value = grid[i % limit][j % limit] + int(j / limit) + int(i/limit)
            if new_value > 9: new_value -= 9
            new_grid[i].append(new_value)
    return traversal(new_grid)



if __name__ == "__main__":
    print("Solution part one: %d" % partOne())
    print("Solution part two: %d" % partTwo())