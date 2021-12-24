import sys
import math
def partOneAndTwo(partOne):
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    initial_pos = [int(x) for x in lines[0].split(',')]
    min_pos, max_pos = min(initial_pos), max(initial_pos)


    min_cost = math.inf
    for i in range(min_pos, max_pos+1):
        cur_pos = i
        cost = 0
        for j in range(len(initial_pos)):

            if partOne: cost += abs(cur_pos - initial_pos[j])
            else:
                distance = abs(cur_pos - initial_pos[j])
                cost += ((distance+1)*distance)/2
        if cost < min_cost:
            min_cost = cost
    return min_cost





if __name__ == "__main__":
    print("Solution part one: %d" %partOneAndTwo(True))
    print("Solution part two: %d" %partOneAndTwo(False))

