import sys

class Board():

    def __init__(self):
        self.field = [[0]]
        self.max = [0,0]
        self.marked = 0


    def add(self, start, end, partOne):
        self.adjustField(start, end)
        if start[0] == end[0] or start[1] == end[1]:
            self.markNoneDiagonalFields(start, end)
        elif not partOne:
            self.markDiagonalFields(start,end)


    def adjustField(self, start, end):
        old_x, old_y = self.max[0], self.max[1]

        x_max = start[0] if start[0] > end[0] else end[0]
        if x_max > self.max[0]: self.max[0] = x_max
        self.processDiffs(old_x, 0)

        y_max = start[1] if start[1] > end[1] else end[1]
        if y_max > self.max[1]: self.max[1] = y_max
        self.processDiffs(old_y, 1)



    def processDiffs(self, old, dim):
        if dim == 0:
            for i in range(old+1, self.max[0]+1):
                self.field.append([0])
        else:
            for i in range(self.max[0] + 1):
                self.field[i].extend([0] * (self.max[1]-len(self.field[i])+1))

    def print_field(self):
        [print(x) for x in self.field]

    def markNoneDiagonalFields(self, start, end):
        x_start, x_end = (start[0], end[0]+1) if start[0] < end[0] else (end[0], start[0]+1)
        y_start, y_end = (start[1], end[1]+1) if start[1] < end[1] else (end[1], start[1]+1)
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                self.field[i][j] += 1
                if self.field[i][j] == 2: self.marked += 1

    def markDiagonalFields(self, start, end):
        increase_x = start[0] < end[0]
        increase_y = start[1] < end[1]

        x,y = start[0], start[1]
        self.field[x][y] += 1
        if self.field[x][y] == 2: self.marked += 1

        while x != end[0] and y != end[1]:
            x = x+1 if increase_x else x-1
            y = y+1 if increase_y else y-1
            self.field[x][y] += 1
            if self.field[x][y] == 2: self.marked += 1


def partOneAndTwo():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    board_one = Board()
    board_two = Board()
    for line in lines:
        coordinates = [[int(x) for x in coordinate] for coordinate in [x.split(",") for x in line.split("->")]]
        board_one.add(coordinates[0], coordinates[1], True)
        board_two.add(coordinates[0], coordinates[1], False)
    #board.print_field()

    print("Solution part one: %d" %board_one.marked)
    print("Solution part two: %d" %board_two.marked)

if __name__ == "__main__":
    partOneAndTwo()
