import math
import sys


operations = {
    0:sum, 1:math.prod,2:min,3:max,
    5:lambda comp_packs: 1 if comp_packs[0] > comp_packs[1] else 0,
    6:lambda comp_packs: 1 if comp_packs[0] < comp_packs[1] else 0,
    7:lambda comp_packs: 1 if comp_packs[0] == comp_packs[1] else 0
}

class Packet:
    def __init__(self, type_id, packet_version):
        self.type_id = type_id
        self.packet_version = packet_version
        self.value = 0
        self.children = []

    def print(self, root=False):
        if not root: print("Packet Version: %d" %self.packet_version)
        for child in self.children: child.print()

    def sum_packet_versions(self, root=False):
        sum = 0
        if not root: sum += self.packet_version
        for child in self.children:
            sum += child.sum_packet_versions()
        return sum

    def evaluate_packet(self):
        if self.type_id == 4:
            return self.value
        return operations[self.type_id]([child.evaluate_packet() for child in self.children])

def scanPack(binary_str, root, pointer = 0):
    packet_version = int(binary_str[pointer:pointer + 3], 2)
    pointer += 3
    type_id = int(binary_str[pointer:pointer + 3], 2)
    pointer += 3
    new_node = Packet(type_id, packet_version)
    if type_id == 4:
        value = ""
        reached_end = False
        while not reached_end:
            reached_end = True if binary_str[pointer] == '0' else False
            value += binary_str[pointer + 1:pointer + 5]
            pointer += 5
        new_node.value = int(value,2)

    else:
        length_id = int(binary_str[pointer], 2)
        pointer += 1
        length_of_subs = int(binary_str[pointer:pointer + 15], 2) if length_id == 0 else int(binary_str[pointer:pointer+11], 2)
        pointer += 15 if length_id == 0 else 11

        while length_of_subs > 0:
            sub_length = scanPack(binary_str, new_node, pointer) - pointer
            pointer += sub_length
            length_of_subs -= sub_length if length_id == 0 else 1

    root.children.append(new_node)
    return pointer


def solution(partOne):
    with open(sys.argv[1]) as f:
        binary_str = f'{int(f.readline(), 16):0>b}'
    zeros_to_add = (4-len(binary_str) % 4) % 4
    for i in range(zeros_to_add): binary_str = "0" + binary_str
    root = Packet(0,-1)
    scanPack(binary_str, root)
    #root.print(True)
    if partOne: return root.sum_packet_versions(True)
    else: return root.evaluate_packet()


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
    return 0



if __name__ == "__main__":
    print("Solution part one: %d" % solution(True))
    print("Solution part two: %d" % solution(False))
