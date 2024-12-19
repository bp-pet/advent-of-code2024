import numpy as np

with open('day18real.txt', 'r') as f:
    raw = f.read()

size = (71, 71)
byte_count = 1024

processed = np.array([[int(i) for i in line.split(',')] for line in raw.split('\n')])

maze = np.full(size, '.')

target = np.array(size) - np.ones_like(size)

for i in range(byte_count):
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

print(distances[tuple(target)])