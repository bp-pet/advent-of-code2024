import numpy as np
import networkx as nx

with open('day16\\day16real.txt', 'r') as f:
    raw = f.read()

maze = np.array([list(i) for i in raw.split('\n')])

G = nx.DiGraph()

start = None
ends = None

for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i, j] == '#':
            continue

        if maze[i, j] == 'S':
            start = (i, j, 'e')
        if maze[i, j] == 'E':
            ends = [(i, j, 'e'), (i, j, 'w'), (i, j, 'n'), (i, j, 's')]
        
        # add directions
        G.add_node((i, j, 'e'))
        G.add_node((i, j, 'w'))
        G.add_node((i, j, 'n'))
        G.add_node((i, j, 's'))

        # add rotations
        G.add_edge((i, j, 'e'), (i, j, 'n'), weight=1000)
        G.add_edge((i, j, 'e'), (i, j, 's'), weight=1000)
        G.add_edge((i, j, 'w'), (i, j, 'n'), weight=1000)
        G.add_edge((i, j, 'w'), (i, j, 's'), weight=1000)
        G.add_edge((i, j, 'n'), (i, j, 'e'), weight=1000)
        G.add_edge((i, j, 'n'), (i, j, 'w'), weight=1000)
        G.add_edge((i, j, 's'), (i, j, 'e'), weight=1000)
        G.add_edge((i, j, 's'), (i, j, 'w'), weight=1000)

# add steps
for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i, j] == '#':
            continue
        
        if maze[i, j + 1] != '#':
            G.add_edge((i, j, 'e'), (i, j + 1, 'e'), weight=1)
        if maze[i, j - 1] != '#':
            G.add_edge((i, j, 'w'), (i, j - 1, 'w'), weight=1)
        if maze[i - 1, j] != '#':
            G.add_edge((i, j, 'n'), (i - 1, j, 'n'), weight=1)
        if maze[i + 1, j] != '#':
            G.add_edge((i, j, 's'), (i + 1, j, 's'), weight=1)


distances = []
for end in ends:
    distances.append(nx.shortest_path_length(G, start, end, weight='weight'))
print(min(distances))