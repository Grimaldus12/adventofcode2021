import os
import sys

def partOne():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    x, depth = 0,0
    for line in lines:
        operation = line.split(" ")[0]
        amount = int(line.split(" ")[1])
        if operation == "forward": x += amount
        elif operation == "down": depth += amount
        else: depth -= amount

    print("Solution part 1: %d" %(x*depth))


def partTwo():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    x, depth, aim = 0, 0, 0
    for line in lines:
        operation = line.split(" ")[0]
        amount = int(line.split(" ")[1])

        if operation == "forward":
            depth += (amount*aim)
            x += amount
        elif operation == "down":
            aim += amount
        else:
            aim -= amount


    print("Solution part 2: %d" %(x*depth))


if __name__ == "__main__":
    partTwo()
