import sys
from copy import deepcopy

def parse_input(input):
    mapping = {'v':1,'>':2,'.':0}
    grid = []
    for line in input:
        grid.append([mapping[c] for c in line.strip()])
    return grid


def move_south(grid):
    new_grid = deepcopy(grid)
    movement = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and grid[(i + 1) % len(grid)][j] == 0:
                new_grid[(i + 1) % len(grid)][j] = 1
                new_grid[i][j] = 0
                movement = True
    return movement, new_grid


def move_east(grid):
    new_grid = deepcopy(grid)
    movement = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2 and grid[i][(j+1)%len(grid[0])] == 0:
                new_grid[i][(j+1)%len(grid[0])] = 2
                new_grid[i][j] = 0
                movement = True
    return movement, new_grid



def solution():
    with open(sys.argv[1]) as f:
        input = f.readlines()

    grid = parse_input(input)
    movement = True
    steps = 0
    while movement:
        steps += 1
        movement_east, grid = move_east(grid)
        movement_south, grid = move_south(grid)
        if not movement_south and not movement_east: movement = False
    return steps



if __name__ == "__main__":
    part1 = solution()
    print("Solution part one: %d" %part1)
