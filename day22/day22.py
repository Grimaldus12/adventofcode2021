import collections
import sys


class Cuboid:

    def __init__(self, limits, state):
        self.x_min, self.x_max = limits[0], limits[1]
        self.y_min, self.y_max = limits[2], limits[3]
        self.z_min, self.z_max = limits[4], limits[5]
        self.state = state

    def __repr__(self):
        return "x:" + str(self.x_min) + "," + str(self.x_max) + " y:" + str(self.y_min) + "," + str(self.y_max) + " z:" + str(self.z_min) + "," + str(self.z_max)

    def __eq__(self, other):
        return self.x_min == other.x_min and self.x_min == other.x_max and self.y_min == other.y_min and self.y_max == other.y_max and \
               self.z_min == other.z_min and self.z_max == other.z_max

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x_min, self.x_max, self.y_min, self.y_max, self.z_min, self.z_max))

    def find_intersection(self, cuboid):
        intersect_x_min = max(self.x_min, cuboid.x_min)
        intersect_x_max = min(self.x_max, cuboid.x_max)
        intersect_y_min = max(self.y_min, cuboid.y_min)
        intersect_y_max = min(self.y_max, cuboid.y_max)
        intersect_z_min = max(self.z_min, cuboid.z_min)
        intersect_z_max = min(self.z_max, cuboid.z_max)

        if intersect_x_min <= intersect_x_max and intersect_y_min <= intersect_y_max and intersect_z_min <= intersect_z_max:
            return Cuboid([intersect_x_min, intersect_x_max, intersect_y_min, intersect_y_max, intersect_z_min, intersect_z_max],cuboid.state)
        return None

    def volume(self,sign):
        return (self.x_max -self.x_min +1) * (self.y_max -self.y_min +1) *(self.z_max -self.z_min +1) * sign


def parse_cuboid(line):
    str_split = line.strip().split(" ")
    state = -1 if str_split[0] == "off" else 1
    coord_split = str_split[1].split(",")
    x_min, x_max = int(coord_split[0].split("=")[1].split("..")[0]), int(coord_split[0].split("=")[1].split("..")[1])
    y_min, y_max = int(coord_split[1].split("=")[1].split("..")[0]), int(coord_split[1].split("=")[1].split("..")[1])
    z_min, z_max = int(coord_split[2].split("=")[1].split("..")[0]), int(coord_split[2].split("=")[1].split("..")[1])
    return Cuboid([x_min, x_max, y_min, y_max, z_min, z_max], state)



def solution(bounds):
    with open(sys.argv[1]) as f:
        input = f.readlines()

    cuboids = collections.Counter()
    for line in input:
        cuboid = parse_cuboid(line)
        if bounds and (cuboid.x_min > 50 or cuboid.x_min < -50): continue
        new_cuboids = collections.Counter()
        for other, sign in cuboids.items():
            intersection = cuboid.find_intersection(other)
            if intersection is not None:
                intersection.state = sign
                new_cuboids[intersection] -= intersection.state
        if cuboid.state == 1:
            new_cuboids[cuboid] += cuboid.state
        cuboids.update(new_cuboids)

    return sum(cuboid.volume(sign) for cuboid,sign in cuboids.items())


if __name__ == "__main__":
    part1 = solution(True)
    part2 = solution(False)
    print("Solution part one: %d" %part1)
    print("Solution part two: %d" %part2)
