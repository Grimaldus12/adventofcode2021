import itertools

new_throws = list(itertools.product([1, 2, 3], repeat=3))
sum_throws = [sum(_) for _ in new_throws]
freq_throws = {_: sum_throws.count(_) for _ in set(sum_throws)}
# print(freq_throws)

import functools


#@functools.cache
def calculate_number_of_wins(start_score_1, start_pos_1, start_score_2, start_pos_2, turn, verbose=0):
    """Having a three sided Dirac cube, where at each throw it splits into
    three.

    The idea is to calculate how many games happens with the initial player
    scores. Even though it feels random, the combinations of throws is
    deterministic and based on the initial positions of players we can
    determine if the player will win from the current setting or not.

    Since the game is played the same way, each player on their turn roles
    the dice three times.

    This means that from single player turn, we get 27 new games or in other
    words the combination of throws of 1 2 3. We can further simplify that
    instead of throws we check the sums of throws. And this reduces it to:
        # rows: frequency
        {
         3: 1,
         4: 3,
         5: 6,
         6: 7,
         7: 6,
         8: 3,
         9: 1
        }

    Arguments:
        score_1
        pos_1
        score_2
        pos_2
        roll - dice current roll

    """
    _c = 0

    for el in freq_throws:
        if verbose:
            print(el)
        pos_1 = start_pos_1
        pos_2 = start_pos_2
        score_1 = start_score_1
        score_2 = start_score_2
        # roll += el
        if turn == 0:  # Player 1
            pos_1 += el
            r = pos_1 % 10
            if r == 0:
                score_1 += 10
            else:
                score_1 += r

            if score_1 >= 21:
                _c += freq_throws[el]
            else:
                _c += freq_throws[el] * calculate_number_of_wins(score_1, pos_1, score_2, pos_2, 1)
        else:
            pos_2 += el
            r = pos_2 % 10
            if r == 0:
                score_2 += 10
            else:
                score_2 += r

            if score_2 >= 21:
                continue  # Do not count
            else:
                _c += freq_throws[el] * calculate_number_of_wins(score_1, pos_1, score_2, pos_2, 0)

    return _c


pos_1 = 4
pos_2 = 2
score_1 = 0
score_2 = 0
wins = calculate_number_of_wins(score_1, pos_1, score_2, pos_2, 0, verbose=1)
print(wins)