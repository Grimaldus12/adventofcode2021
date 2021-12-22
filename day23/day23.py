import sys



def solution():
    with open(sys.argv[1]) as f:
        input = f.readlines()

    return 0


if __name__ == "__main__":
    part1 = solution()
    part2 = solution()
    print("Solution part one: %d" %part1)
    print("Solution part two: %d" %part2)
