import sys

class Board():

    def __init__(self, lines):
        self.horizontals, self.verticals = [], []
        self.winning_rows, self.winning_columns = {}, {}
        self.find_lines(lines)

    def find_lines(self, lines):
        self.horizontals = [list(map(int, filter(None,line.strip().split(" ")))) for line in lines]
        self.verticals = [[row[i] for row in self.horizontals] for i in range(len(lines))]

    def search_input(self, input):
        minimum_draws = len(input)
        for i in range(len(self.horizontals)):
            matches_horizontal, matches_vertical = 0, 0
            max_idx_row, max_idx_col = 0, 0
            for j in range(len(self.horizontals[0])):
                if self.horizontals[i][j] in input:
                    idx = input.index(self.horizontals[i][j])
                    matches_horizontal += 1
                    if max_idx_row < idx: max_idx_row = idx
                if  self.verticals[i][j] in input:
                    idx = input.index(self.verticals[i][j])
                    matches_vertical += 1
                    if max_idx_col < idx: max_idx_col = idx

            if matches_horizontal == 5:
                self.winning_rows[i] = max_idx_row
                if max_idx_row < minimum_draws: minimum_draws = max_idx_row
            if matches_vertical == 5:
                self.winning_columns[i] = max_idx_col
                if max_idx_col < minimum_draws: minimum_draws = max_idx_col
        return minimum_draws

    def calculate_win(self, input):
        total_sum = sum(map(sum, self.horizontals))
        marked_sum = 0
        for i in range(len(self.horizontals)):
            for j in range(len(self.horizontals[0])):
                if self.horizontals[i][j] in input: marked_sum += self.horizontals[i][j]
        return total_sum-marked_sum


def partOneAndTwo():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    input = list(map(int, lines[0].split(',')))
    boards = []
    for i in range(1, len(lines)):
        if lines[i].strip() == "":
            boards.append(Board(lines[i+1:i+6]))

    least_draws,most_draws = len(input), 0
    best_board,worst_board = None, None
    for board in boards:
        cur_minimum = board.search_input(input)
        if cur_minimum < least_draws:
            least_draws = cur_minimum
            best_board = board
        if cur_minimum > most_draws:
            most_draws = cur_minimum
            worst_board = board

    score_of_unmarked_best = best_board.calculate_win(input[:least_draws+1])
    score_of_unmarked_worst = worst_board.calculate_win(input[:most_draws+1])

    print("Solution part one: %d" %(score_of_unmarked_best * input[least_draws]))
    print("Solution part two: %d" % (score_of_unmarked_worst * input[most_draws]))

if __name__ == "__main__":
    partOneAndTwo()
