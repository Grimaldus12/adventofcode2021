import sys




def partOne():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    bracket_pairs = {'(':')','[':']','{':'}','<':'>'}
    point_table = {')':3, ']':57, '}':1197, '>':25137}

    syntax_error_score = 0
    for line in lines:
        opened_chunks = []

        for c in line.strip():
            if c in ['{', '[','(','<']:
                opened_chunks.append([c,''])
            else:
                if bracket_pairs[opened_chunks[-1][0]] == c: del opened_chunks[-1]
                else:
                    syntax_error_score += point_table[c]
                    break
    return syntax_error_score


def partTwo():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    bracket_pairs = {'(':')','[':']','{':'}','<':'>'}
    point_table = {'(':1, '[':2, '{':3, '<':4}
    scores = []
    for line in lines:
        opened_chunks = []
        corrupted = False
        for c in line.strip():
            if c in ['{', '[','(','<']:
                opened_chunks.append([c,''])
            else:
                if bracket_pairs[opened_chunks[-1][0]] == c:
                    del opened_chunks[-1]
                else:
                    corrupted = True
                    break
        if corrupted: continue
        incomplete_score = 0
        for i in range(len(opened_chunks) - 1, -1, -1):
            incomplete_score *= 5
            incomplete_score += point_table[opened_chunks[i][0]]
        scores.append(incomplete_score)

    scores.sort()
    return scores[int(len(scores)/2)]


if __name__ == "__main__":
    #sum_part_one, product_part_two = partOne()
    print("Solution part one: %d" %partOne())
    print("Solution part two: %d" %partTwo())

