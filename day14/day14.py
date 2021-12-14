import sys
from collections import defaultdict

def solution(iterations):
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    template = lines[0].strip()
    rules = {}
    for i in range(2,len(lines)):
        string_split = lines[i].strip().split(" -> ")
        rules[string_split[0]] = string_split[1]

    last_iter = template.strip()
    last_pairs = defaultdict(int)
    for i in range(len(last_iter)-1):
        pair = last_iter[i] + last_iter[i+1]
        last_pairs[pair] += 1
    for i in range(iterations):
        cur_pairs = defaultdict(int)
        for pair in last_pairs.keys():
            substitution = rules[pair]
            a, b = pair[0]+substitution, substitution + pair[1]
            cur_pairs[a] += 1 * last_pairs[pair]
            cur_pairs[b] += 1 * last_pairs[pair]
        last_pairs = cur_pairs.copy()

    counts = defaultdict(int)
    for pair in last_pairs:
        counts[pair[0]] += 1 * last_pairs[pair]
    counts[template[-1]] += 1
    count = list(counts.values())
    count.sort()
    return count[-1] - count[0]


if __name__ == "__main__":
    print("Solution part one: %d" %solution(10))
    print("Solution part two: %d" %solution(40))

