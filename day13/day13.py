import sys
import numpy as np


def solution(only_one_fold):
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    max_x, max_y = 0,0
    points = []
    start_folds = 0
    for i,line in enumerate(lines):
        if line.strip()  == "":
            start_folds = i + 1
            break
        point = [int(line.strip().split(",")[0]), int(line.strip().split(",")[1])]
        if point[0] > max_x: max_x = point[0]
        if point[1] > max_y: max_y = point[1]
        points.append(point)

    grid = np.zeros((max_y+1, max_x+1), dtype=bool)
    for point in points: grid[point[1], point[0]] = True

    last_grid = grid.copy()
    for i in range(start_folds, len(lines)):
        fold = lines[i].split(" ")[2].strip().split("=")
        dots = 0
        if fold[0] == 'y':
            new_grid = np.zeros((int(fold[1]), last_grid.shape[1]), dtype=bool)
            for j in range(int(fold[1])):
                new_grid[j,:] = np.logical_or(last_grid[j,:],last_grid[last_grid.shape[0]-1-j,:])
            dots = np.count_nonzero(new_grid)
            last_grid = new_grid.copy()
        else:
            new_grid = np.zeros((last_grid.shape[0], int(fold[1])), dtype=bool)
            for j in range(int(fold[1])):
                new_grid[:,j] = np.logical_or(last_grid[:,j], last_grid[:,last_grid.shape[1] - 1 - j])
            dots = np.count_nonzero(new_grid)
            last_grid = new_grid.copy()

        if only_one_fold: return dots

    with open("output.txt", 'w') as file:
        array_as_string = '\n'.join(' '.join('%d' %x for x in y) for y in last_grid.astype(int)).replace("0", ".")
        file.write(array_as_string)
    return 0





if __name__ == "__main__":
    print("Solution part one: %d" %solution(True))
    solution(False)
    print("Solution part two see output.txt")

