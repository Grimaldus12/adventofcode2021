import sys


adjacent_nodes = {}
paths_found = 0

def dfs_modified(node, visited_nodes, visited_twice):
    global adjacent_nodes, paths_found
    cur_visited = visited_nodes.copy()
    cur_visited.append(node)
    if node == 'end':
        paths_found += 1
        return
    for destination in adjacent_nodes[node]:
        if destination.islower() and destination in cur_visited:
            if not visited_twice and destination not in ['start', 'end']:
                dfs_modified(destination, cur_visited, True)
            else:
                continue
        else:
            dfs_modified(destination, cur_visited, visited_twice)



def solution(allow_double_visit):
    global adjacent_nodes, paths_found
    paths_found = 0
    adjacent_nodes = {}
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    for line in lines:
        node1 = line.split("-")[0]
        node2 = line.split("-")[1].strip()
        if node1 not in adjacent_nodes.keys(): adjacent_nodes[node1] = [node2]
        else: adjacent_nodes[node1].append(node2)
        if node2 not in adjacent_nodes.keys(): adjacent_nodes[node2] = [node1]
        else: adjacent_nodes[node2].append(node1)

    cur_node = 'start'
    if not allow_double_visit:
        dfs_modified(cur_node, [], True)
    else:
        dfs_modified(cur_node, [], False)
    return paths_found



if __name__ == "__main__":
    print("Solution part one: %d" %solution(False))
    print("Solution part two: %d" %solution(True))

