import sys


def has_flash_ready(grid):
    for k in range(len(grid)):
        for l in range(len(grid[0])):
            if grid[k][l] == 10: return True


def update_neighbors(k, l, grid):
    for j in range(k-1,k+2):
        for m in range(l-1,l+2):
            if j == k and l == m: continue
            elif j >= len(grid) or j < 0 or m >= len(grid[0]) or m < 0: continue
            elif grid[j][m] == 0: continue
            elif grid[j][m] != 10: grid[j][m] += 1


def flash_octos(grid):
    flashed_octos = 0
    for k in range(len(grid)):
        for l in range(len(grid[0])):
            if grid[k][l] == 10:
                flashed_octos += 1
                grid[k][l] = 0
                update_neighbors(k,l,grid)
    return flashed_octos


def increase_energy(grid):
    for k in range(len(grid)):
        for l in range(len(grid[0])):
            grid[k][l] += 1


def partOne():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    grid = [[int(line[i]) for i in range(len(line.strip()))] for line in lines]

    total_flashes = 0
    i = 0
    while True:
        i += 1
        increase_energy(grid)
        flashes = 0
        while has_flash_ready(grid):
            flashes += flash_octos(grid)
        if i <= 100: total_flashes += flashes
        if flashes == len(grid)*len(grid[0]):
            break

    return total_flashes, i




if __name__ == "__main__":
    sol_one, sol_two = partOne()
    print("Solution part one: %d" %sol_one)
    print("Solution part two: %d" %sol_two)

