import sys

def partOneAndTwo(generations):
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    fishes = [int(x) for x in lines[0].split(",")]
    living_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for fish in fishes:
        living_dict[fish] += 1

    for i in range(generations):
        produced_fish = living_dict[0]
        living_dict[7] += living_dict[0]
        for j in range(1,9):
            living_dict[j-1] = living_dict[j]
        living_dict[8] = produced_fish

    return sum(living_dict.values())

if __name__ == "__main__":
    print("Solution part one: %d" %partOneAndTwo(80))
    print("Solution part two: %d" %partOneAndTwo(256))

