with open('day10\\day10real.txt', 'r') as f:
    raw = f.read()

import numpy as np
import networkx as nx

grid = np.array([[int(j) if j != '.' else -1 for j in list(i)] for i in raw.split('\n')])

G = nx.DiGraph()

origins = []
targets = []

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i, j] != -1:
            name = f'{i}-{j}-{grid[i, j]}'
            G.add_node(f'{i}-{j}-{grid[i, j]}')
            if grid[i, j] == 0:
                origins.append(name)
            if grid[i, j] == 9:
                targets.append(name)

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        origin = (i, j)
        if grid[origin] == -1:
            continue
        for target in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if target[0] < 0 or target[0] >= grid.shape[0] or target[1] < 0 or target[1] >= grid.shape[0] or grid[origin] + 1 != grid[target]:
                continue
            G.add_edge(f'{i}-{j}-{grid[origin]}', f'{target[0]}-{target[1]}-{grid[target]}')

result = 0
for o in origins:
    for t in targets:
            result += len(list(nx.all_simple_paths(G, o, t)))
print(result)