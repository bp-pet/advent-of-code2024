"""
Thought the question said that one couldn't exit and re-enter a wall during a cheat.
"""
import numpy as np
import networkx as nx

with open('day20\\day20example.txt', 'r') as f:
    raw = f.read()

maze = np.array([list(i) for i in raw.split('\n')])

current, end = None, None
maze_num = np.full(maze.shape, -1)

for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i, j] == 'S':
            current = np.array((i, j))
        if maze[i, j] == 'E':
            end = np.array((i, j))
        if maze[i, j] in ['.', 'S', 'E']:
            maze_num[i, j] = -2

counter = 0
while True:
    maze_num[tuple(current)] = counter
    neighbor = None
    for offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if maze_num[tuple(current + np.array(offset))] == -2:
            neighbor = current + np.array(offset)
            break
    if neighbor is None:
        break
    current = neighbor
    counter += 1


G = nx.Graph()

for i in range(maze_num.shape[0]):
    for j in range(maze_num.shape[1]):
        if maze_num[i, j] != -1:
            continue
        current = np.array([i, j])
        G.add_node((i, j), min_entry=None, max_entry=None)
        for offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = tuple(current + np.array(offset))
            if new_pos[0] < 0 or new_pos[0] >= maze.shape[0] or new_pos[1] < 0 or new_pos[1] >= maze.shape[1]:
                continue
            if maze_num[new_pos] != -1:
                # neighbor is path
                if G.nodes[tuple(current)]['min_entry'] is None or G.nodes[tuple(current)]['min_entry'] > maze_num[tuple(new_pos)]:
                    G.nodes[tuple(current)]['min_entry'] = maze_num[tuple(new_pos)]
                if G.nodes[tuple(current)]['max_entry'] is None or G.nodes[tuple(current)]['max_entry'] < maze_num[tuple(new_pos)]:
                    G.nodes[tuple(current)]['max_entry'] = maze_num[tuple(new_pos)]
            else:
                # neighbor is wall
                G.add_edge(tuple(current), tuple(new_pos))


for entry_node in G.nodes:
    entry_val = G.nodes[entry_node]['min_entry']
    if entry_val is None:
        continue
    ego = nx.ego_graph(G, entry_node, 20 - 2)
    exit_node = max(ego.nodes, key=lambda x: ego.nodes[x]['max_entry'] if ego.nodes[x]['max_entry'] is not None else -1)
    distance_in_wall = nx.shortest_path_length(ego, entry_node, exit_node)
    exit_val = G.nodes[exit_node]['max_entry']
    saved_time = exit_val - entry_val - distance_in_wall - 2
    # if saved_time > 70:
    #     print(saved_time, entry_node, exit_node)