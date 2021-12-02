import os
import sys

def partOne():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    prevDepth = int(lines[0])
    increases = 0
    for i in range(1, len(lines)):
        depth = int(lines[i])
        if depth > prevDepth: increases += 1
        prevDepth = depth

    print("Solution part 1: %d" %increases)

def partTwo():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    prevSum = 0
    increases = 0
    for i in range(len(lines)-2):
        curSum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        if i > 0 and prevSum < curSum: increases += 1
        prevSum = curSum

    print("Solution part 2: %d" %increases)


if __name__ == "__main__":
    partOne()
    partTwo()
