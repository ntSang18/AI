# Tìm kiếm theo chiều sâu (Deep first search)
from unittest import result
from sympy import GoldenRatio, false


def DFS(initialState, goal):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(len(frontier) - 1)
        explored.append(state)
        if(goal) == state:
            return explored
        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)
    return false


def DFS2(start, goal, path, level, maxD):
    path.append(start)
    if start == goal:
        return path
    if level == maxD:
        return false
    for child in graph[start]:
        if DFS2(child, goal, path, level+1, maxD):
            return path
        path.pop()
    return false


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': ['J', 'K'],
        'F': ['L', 'M'],
        'G': ['N', 'O'],
        'H': [],
        'I': [],
        'J': [],
        'K': [],
        'L': [],
        'M': [],
        'N': [],
        'O': []}
    result = DFS('A', 'H')
    if result:
        s = 'explored: '
        for i in result:
            s += i + ''
            print(s)
    else:
        print("404 Not Found!")
