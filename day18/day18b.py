import numpy as np

# with open('day18example.txt', 'r') as f:
#     raw = f.read()
# size = (7, 7)
# byte_count = 12

with open('day18real.txt', 'r') as f:
    raw = f.read()
size = (71, 71)
byte_count = 1024

processed = np.array([[int(i) for i in line.split(',')] for line in raw.split('\n')])

def get_distance(modified_byte_count):

    maze = np.full(size, '.')

    target = np.array(size) - np.ones_like(size)

    for i in range(modified_byte_count):
        maze[tuple(processed[i, :])] = '#'

    unvisited = []
    distances = np.full(size, np.inf)
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if maze[i, j] == '.':
                unvisited.append((i, j))
                distances[i, j] = np.inf
    distances[0, 0] = 0

    while True:
        if len(distances) == 0:
            break
        current = np.array(min(unvisited, key=lambda x: distances[x]))
        if (current == target).all() or distances[tuple(current)] == np.inf:
            break
        for offset in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            neighbor = current + np.array(offset)
            if tuple(neighbor) in unvisited and distances[tuple(neighbor)] > 1 + distances[tuple(current)]:
                distances[tuple(neighbor)] = 1 + distances[tuple(current)]
        unvisited.remove(tuple(current))

    return distances[tuple(target)]


start_val = byte_count
end_val = processed.shape[0]

step = 1000
current_val = start_val
"""Speed up search by starting with step 1000 until getting to a number of walls that makes it impossible, then go back 1000 and change step to 100, etc."""
while True:
    if step < 1:
        break
    current_val -= step
    for i in range(step * 10):
        current_val += step
        print(f'Checking {current_val}')
        if current_val > processed.shape[0] or get_distance(current_val) == np.inf:
            if step == 1:
                print(f'Found {processed[current_val - 1, :]}')
            current_val -= step
            step = step // 10
            break