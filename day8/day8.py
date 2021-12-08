import sys
import math
def partOne():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    output_values = [line.split('|')[1].strip() for line in lines]
    unique_digits = 0
    for output_value in output_values:
        for digit in output_value.split(" "):
            if len(digit) in [2,3,4,7]:
                unique_digits += 1
    return unique_digits


def get_digit(active_positions):
    digit_map = {0:[0,1,2,4,5,6],1:[2,5],2:[0,2,3,4,6],3:[0,2,3,5,6],
                 4:[1,2,3,5],5:[0,1,3,5,6],6:[0,1,3,4,5,6],7:[0,2,5],
                 8:[0,1,2,3,4,5,6],9:[0,1,2,3,5,6]}
    for digit in digit_map.keys():
        if len(active_positions) == len(digit_map[digit]) and all(x in active_positions for x in digit_map[digit]):
            return digit


def partTwo():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    known_freq = {8:-1, 6:1,7:-2,4:4,9:5}
    sum_of_codes = 0
    for line in lines:
        frequencies = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
        patterns = line.split("|")[0].split(" ")
        encoded = line.split("|")[1].strip().split(" ")
        assignment = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
        top_right_bar = []
        middle_bars = []
        for pattern in patterns:
            for char in pattern:
                frequencies[char] += 1
        for key in frequencies.keys():
            assignment[key] = known_freq[frequencies[key]]
            if assignment[key] == -1: top_right_bar.append(key)
            if assignment[key] == -2: middle_bars.append(key)

        for pattern in patterns:
            if len(pattern) == 8: continue
            elif len(pattern) == 5:
                active_positions = []
                for char in pattern:
                    if assignment[char] != -1 and assignment[char] != -2:
                        active_positions.append(assignment[char])
                if all(x in active_positions  for x in [1,5]):
                    if top_right_bar[0] in pattern:
                        assignment[top_right_bar[0]] = 0
                        assignment[top_right_bar[1]] = 2
                    elif top_right_bar[1] in pattern:
                        assignment[top_right_bar[0]] = 2
                        assignment[top_right_bar[1]] = 0
            elif len(pattern) == 4:
                if middle_bars[0] in pattern:
                    assignment[middle_bars[0]] = 3
                    assignment[middle_bars[1]] = 6
                elif middle_bars[1] in pattern:
                    assignment[middle_bars[0]] = 6
                    assignment[middle_bars[1]] = 3

        code_str = ""
        for code in encoded:
            active_positions = []
            for char in code:
                active_positions.append(assignment[char])
            digit = get_digit(active_positions)
            code_str += str(digit)
        sum_of_codes += int(code_str)
    return sum_of_codes


if __name__ == "__main__":

    print("Solution part one: %d" %partOne())
    print("Solution part two: %d" %partTwo())

