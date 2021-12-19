import math
import sys
from collections import defaultdict
from itertools import combinations

class Coordinate:
    def __init__(self, x,y,z):
        self.x, self.y, self.z = x,y,z

    def __repr__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z)

    def offset(self, distance):
        return Coordinate(self.x+distance.x, self.y+distance.y, self.z+distance.z)

    def roll(self):
        return Coordinate(self.x, -self.z, self.y)

    def turn(self):
        return Coordinate(-self.z, self.y, self.x)

    def getTransform(self):
        transforms = []
        t = self
        for cycle in range(2):
            for step in range(3):
                t = t.roll()
                transforms.append(t)
                for i in range(3):
                    t = t.turn()
                    transforms.append(t)
            t = t.roll().turn().roll()
        return transforms


    def distance(self, other_coord):
        return Coordinate(self.x - other_coord.x, self.y - other_coord.y, self.z - other_coord.z)

    def manhattan(self, other_coord):
        return abs(self.x-other_coord.x) + abs(self.y-other_coord.y) + abs(self.z-other_coord.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash((self.x, self.y, self.z))

class Scanner:

    def __init__(self, name, coords_list):
        self.name = name
        if all(isinstance(coord, str) for coord in coords_list):
            self.coords = [Coordinate(int(coord.strip().split(",")[0]), int(coord.strip().split(",")[1]), int(coord.strip().split(",")[2])) for coord in coords_list]
        else:
            self.coords = coords_list

    def __repr__(self):
        string = self.name + "\n"
        for coord in self.coords: string += coord.__repr__()
        return string

    def transform(self):
        possibilities = [Scanner(self.name, []) for k in range(24)]
        for coord in self.coords:
            list_of_transforms = coord.getTransform()
            for i in range(24):
                possibilities[i].addCoord(list_of_transforms[i])
        return possibilities


    def addCoord(self, coord):
        self.coords.append(coord)

    def addOtherCoordinates(self, other, distance):
        for coord in other.coords:
            offset_coord = coord.offset(distance)
            if offset_coord in self.coords: continue
            self.addCoord(offset_coord)

    def compareScanner(self, other_scanner):
        distance_dict = defaultdict(int)
        for coord in self.coords:
            for other_coord in other_scanner.coords:
                dist = coord.distance(other_coord)
                distance_dict[dist] += 1
        matching_coords = None
        observed_matching = 0
        for key in distance_dict:
            if distance_dict[key] >= 12:
                matching_coords = key
                observed_matching += 1
        if matching_coords is None: return None
        elif observed_matching > 1:  raise ValueError("More than one distance found")
        else: return matching_coords




def get_orientations(s):
    return s.transform()


def solution():
    with open(sys.argv[1]) as f:
        input = f.readlines()

    scanner = []
    current_scanner_lines = []
    current_name = ""
    for line in input:
        if len(line.strip()) == 0:
            scanner.append(Scanner(current_name,current_scanner_lines))
        elif "---" in line:
            current_name = line
            current_scanner_lines = []
        else:
            current_scanner_lines.append(line)
    scanner.append(Scanner(current_name,current_scanner_lines))

    base_scanner = scanner[0]
    scanner.remove(scanner[0])

    scanner_positions = defaultdict()
    scanner_positions[base_scanner.name] = Coordinate(0,0,0)
    while len(scanner) != 0:
        for s in scanner:
            for orientation in get_orientations(s):
                distance = base_scanner.compareScanner(orientation)
                if distance is None: continue
                base_scanner.addOtherCoordinates(orientation, distance)
                scanner_positions[s.name] = distance
                scanner.remove(s)
                break
            else:
                continue
            break


    best_manhattan = 0
    for pair in list(combinations(scanner_positions.keys(), 2)):
        manhattan = scanner_positions[pair[0]].manhattan(scanner_positions[pair[1]])
        if manhattan > best_manhattan: best_manhattan = manhattan

    #print(best_manhattan)
    return len(base_scanner.coords), best_manhattan


if __name__ == "__main__":
    part1, part2 = solution()
    print("Solution part one: %d" %part1)
    print("Solution part two: %d" %part2)
