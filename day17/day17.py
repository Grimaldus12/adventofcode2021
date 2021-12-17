import sys
from itertools import product


def see_if_target_hit(dx,dy,target):
    x_min, x_max, y_min, y_max = target
    x,y = 0,0
    while x <= x_max and y >= y_max:
        x += dx
        y += dy
        dx = max(0,dx-1)
        dy -= 1
        if x_min <= x <= x_max and y_min >= y >= y_max:
            return True
    return False


def solution(partOne):
    with open(sys.argv[1]) as f:
        input = f.readline()
    x, y = input.split('=')[1], input.split('=')[2]
    x_min, x_max = int(x.split('..')[0]), int(x.split('..')[1].split(",")[0])
    y_min, y_max = int(y.split('..')[1]), int(y.split('..')[0])
    if partOne:
        d_y = (-1*y_max) - 1
        max_height = ((d_y+1)*d_y)/2
        return max_height
    else:
        valid_veloctities = []
        for dx,dy in product(range(x_max+1), range(-1000,1000)):
            if see_if_target_hit(dx, dy, (x_min,x_max,y_min,y_max)):
                valid_veloctities.append((dx,dy))
        return len(valid_veloctities)


if __name__ == "__main__":
    print("Solution part one: %d" % solution(True))
    print("Solution part two: %d" % solution(False))
