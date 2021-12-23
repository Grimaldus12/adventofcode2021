import sys
from collections import deque

# inspiration taken from https://github.com/kupuguy/aoc2021/tree/main/src for the four base rules of the game

costs = {'A':1,'B':10,'C':100,'D':1000}

def parse_input(input, folded=False):
    board = input[1].strip()[1:-1]
    for i in [3,5,7,9]:
        board += input[2].strip()[i]
        if folded:
            board += input[3].strip()[i]
            board += input[4].strip()[i]
        board += input[5].strip()[i]
    return board

def new_board(board, pos1, pos2):
    n_board = list(board)
    n_board[pos1], n_board[pos2] = board[pos2], board[pos1]
    return "".join(n_board)

def moves(board, n=4):
    targets = {}
    buckets = {}
    tops = []
    entrances = {}

    if n == 2:
        targets = {'A': [11, 12], 'B': [13, 14], 'C': [15, 16], 'D': [17, 18]}
        entrances = {11: 2, 13: 4, 15: 6, 17: 8}
        tops = [11,13,15,17]
        buckets = {11:'A',13:'B',15:'C',17:'D'}
    elif n == 4:
        targets = {'A': [11, 12,13,14], 'B': [15,16,17,18], 'C': [19,20,21,22], 'D': [23,24,25,26]}
        entrances = {11: 2, 15: 4, 19: 6, 23: 8}
        buckets = {11:'A',15:'B',19:'C',23:'D'}
        tops = [11, 15, 19, 23]

    # move a correctly placed amphipod at the top, down in its room
    for top_of_room in tops:
        if board[top_of_room] != '.' \
                and all(board[top_of_room + in_room] in ['.', board[top_of_room]] for in_room in range(1,n)) \
                and top_of_room in targets[board[top_of_room]]:
            for i in range(1,n):
                if i == 1 and board[top_of_room+i] != '.': break
                elif n <= 2:
                    yield new_board(board, top_of_room, top_of_room + i), costs[board[top_of_room]] * i
                    return
                if i > 1:
                    if board[top_of_room+i] != '.':
                        yield new_board(board, top_of_room, top_of_room + i-1), costs[board[top_of_room]] * (i-1)
                        return
                    elif i == n-1:
                        yield new_board(board, top_of_room, top_of_room + i), costs[board[top_of_room]] * i
                        return


    # if the room is not yet correctly filled, move the first assigned amphipod to the top
    for top_of_room in tops:
        if board[top_of_room] == '.' and any(board[top_of_room+i] not in (".",buckets[top_of_room]) for i in range(1,n)):
            for i in range(1,n):
                if board[top_of_room+i] != '.':
                    yield new_board(board, top_of_room, top_of_room + i), costs[board[top_of_room + i]] * i
                    return


    # move an amphipod from the hallway to the top element of the correct room if possible
    for hall_pointer in range(11):
            if board[hall_pointer] == '.': continue
            target_room = targets[board[hall_pointer]][0]
            if board[target_room] != '.' or (board[target_room+1] != '.' and board[target_room+1] != board[hall_pointer]): continue
            entrance = entrances[target_room]
            if entrance > hall_pointer and all(board[h] == '.' for h in range(hall_pointer+1, entrance)):
                yield new_board(board, hall_pointer, target_room), costs[board[hall_pointer]] * (entrance - hall_pointer + 1)
                return
            elif hall_pointer > entrance and all(board[h] == '.' for h in range(entrance, hall_pointer)):
                yield new_board(board, hall_pointer, target_room), costs[board[hall_pointer]] * (hall_pointer - entrance + 1)
                return

    # move a top element of a room to all allowed hallway positions
    for top_of_room in tops:
        if board[top_of_room] == '.': continue
        if top_of_room in targets[board[top_of_room]] and all(board[top_of_room + i] in ('.',board[top_of_room]) for i in range(1,n)): continue
        exit_position = entrances[top_of_room]
        for hall_pointer in range(exit_position-1,-1,-1):
            if hall_pointer in [2,4,6,8]: continue
            if board[hall_pointer] != '.': break
            yield new_board(board, top_of_room, hall_pointer), costs[board[top_of_room]] * (exit_position-hall_pointer+1)
        for hall_pointer in range(exit_position+1, 11):
            if hall_pointer in [2,4,6,8]: continue
            if board[hall_pointer] != '.': break
            yield new_board(board, top_of_room, hall_pointer), costs[board[top_of_room]] * (hall_pointer-exit_position+1)


def solution(partOne):
    with open(sys.argv[1]) as f:
        input = f.readlines()

    board = parse_input(input, not partOne)
    n = 2 if partOne else 4
    visited_state = {board:0}
    queue = deque([board])
    while queue:
        board = queue.popleft()
        cost = visited_state[board]
        for next_move, move_cost in moves(board,n):
            if next_move in visited_state and visited_state[next_move] <= cost + move_cost: continue
            visited_state[next_move] = cost+move_cost
            queue.append(next_move)

    return visited_state["...........AABBCCDD"] if partOne else visited_state["...........AAAABBBBCCCCDDDD"]


if __name__ == "__main__":
    part1 = solution(True)
    part2 = solution(False)
    print("Solution part one: %d" %part1)
    print("Solution part two: %d" %part2)
