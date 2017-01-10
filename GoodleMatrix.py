from collections import deque
"""
Transforming the matrix into a graph of connected nodes happens with only
one iteration over the matrix, and is worth it thanks to the performace
gains we potentially gain over big mazes.
"""

def transform(M):
    # Turn matrix into a graph with each node connected to its non-1 adjacent nodes
    # D: down, U: Up, L:left, R:Right, record these instructions easy for debugging,
    # and len(list of instructions) + 1 will gives us path length
    height = len(M)
    width = len(M[0]) if height else 0
    graph = {(i, j): [M[i][j]] for j in range(width) for i in range(height)}
    for line, col in graph.keys(): # Dictionary with position as keys and value is list of neighbors
        if line < height - 1 and M[line + 1][col] != 1:
            graph[(line, col)].append(("D", (line + 1, col)))
            graph[(line + 1, col)].append(("U", (line, col))) # Add current node as adj to its own adj
        if col < width - 1 and M[line][col + 1] != 1:
            graph[(line, col)].append(("R", (line, col + 1)))
            graph[(line, col + 1)].append(("L", (line, col)))
    return graph


def BFS(M):
    goal = (len(M) - 1, len(M[0]) - 1)
    li = deque([("", (0, 0))]) # init queue with start position
    visits = set() # Keep track of already visited nodes
    graph = transform(M)
    while li:
        path, curr = li.popleft()
        if curr == goal:
            return path
        if curr in visits:
            continue
        visits.add(curr)
        for direction, neighbour in graph[curr][1:]: # Run through neighbours while remembering how we got here
            li.append((path + direction, neighbour))
    return 'impossible'

def answer(M):
    paths = []
    paths.append(BFS(M))
    for i in range(len(M)):
        for j in rnge(len(M[0])):
            if M[i][j] == 1:
                M[i][j] = 0
                paths.append(BFS(M))
                M[i][j] = 1
    paths = [len(path) + 1 for path in paths if path != 'impossible']
    return min(paths)

print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])