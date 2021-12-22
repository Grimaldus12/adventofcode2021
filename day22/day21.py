import sys
from collections import Counter
from itertools import product

#split_freq = Counter(s1+s2+s3 for (s1,s2,s3) in product([1,2,3],repeat=3))
import itertools
new_throws = list(itertools.product([1,2,3], repeat=3))
sum_throws = [sum(_) for _ in new_throws]
split_freq = {_:sum_throws.count(_) for _ in set(sum_throws)}

def play_dirac_game(last_pos_p1, last_pos_p2, last_s_p1, last_s_p2, t):
    counter = 0
    for dirac_roll in split_freq:
        pos_p1, pos_p2, s_p1, s_p2 = last_pos_p1, last_pos_p2, last_s_p1, last_s_p2
        if t == 0:
            pos_p1 = (dirac_roll + pos_p1)%10
            s_p1 += 10 if pos_p1 == 0 else pos_p1
            if s_p1 >= 21:
                counter += split_freq[dirac_roll]
            else:
                counter += split_freq[dirac_roll] * play_dirac_game(pos_p1, pos_p2, s_p1, s_p2, 1)
        else:
            pos_p2 = (dirac_roll + pos_p2) % 10
            s_p2 += 10 if pos_p2 == 0 else pos_p2
            if s_p2 < 21: counter += split_freq[dirac_roll] * play_dirac_game(pos_p1, pos_p2, s_p1, s_p2,0)
    return counter




def partTwo():
    with open(sys.argv[1]) as f:
        input = f.readlines()

    players = {}
    for line in input:
        e = line.strip().split(" ")
        players[int(e[1])] = int(e[-1])

    return play_dirac_game(players[1], players[2], 0, 0, 0)




def partOne():
    with open(sys.argv[1]) as f:
        input = f.readlines()

    players,scores = {},{}
    for line in input:
        e = line.strip().split(" ")
        players[int(e[1])] = int(e[-1])
        scores[int(e[1])] = 0
    print(players)

    die = 0
    turns = 0
    while True:
        for player in players.keys():
            turns += 1
            die1, die2, die3 = die % 100 +1, (die+1) % 100 +1, (die+2) % 100 +1
            player_movement = die1+ die2+ die3
            die = (die+3) % 100
            players[player] = (players[player] +  player_movement) % 10
            if players[player] == 0: players[player] = 10
            scores[player] += players[player]
            if scores[player] >= 1000:
                return scores[3-player] * turns * 3


if __name__ == "__main__":
    part1 =  partOne()
    part2 = partTwo()
    #part2 = solution(50)
    print("Solution part one: %d" %part1)
    print("Solution part two: %d" %part2)
