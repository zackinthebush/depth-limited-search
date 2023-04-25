graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['J'],
    'F': ['K', 'L']
}


def DLS(start, goal, path, level, max_depth):
    print('\nCurrent level-->', level)
    print('Goal node testing for', start)
    path.append(start)
    if start == goal:
        print("Goal test successful")
        return path
    print('Goal node testing failed')
    if level == max_depth:
        return False
    print('\nExpanding the current node', start)
    for child in graph[start]:
        if DLS(child, goal, path, level + 1, max_depth):
            return path
        path.pop()
    return False


start = 'A'
goal = input('Enter the goal node: ')
max_depth = int(input("Enter the maximum depth limit: "))
print()
path = []
res = DLS(start, goal, path, 0, max_depth)
if res:
    print("Path to goal node available")
    print("Path:", path)
else:
    print("No path available for the goal node within the given depth limit")
