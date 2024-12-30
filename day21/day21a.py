"""Couldn't figure out how to do the recursion at first so found hint to use heuristic to choose path. None of the heuristics worked so ended up doing it this way. I create a full graph of all possible inputs and then get shortest path. This however didn't work for part 2 (too many states to even create the graph), so I ended up figuring out the recursion after all."""

import numpy as np
import networkx as nx

total_pads = 5

dpad_buttons = ['L', 'R', 'U', 'D', 'A']
numpad_buttons = [str(i) for i in range(10)] + ['A']

numpad_layout = np.array([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']])
dpad_layout = np.array([[None, 'U', 'A'], ['L', 'D', 'R']])

label_dict = {(1, 0): 'D', (-1, 0): 'U', (0, 1): 'R', (0, -1): 'L'}

G = nx.DiGraph()

for d1 in dpad_buttons:
    for d2 in dpad_buttons:
        for n in numpad_buttons:
            G.add_node(d1 + d2 + n)


def get_edges(layout):
    """For a layout (dpad or numpad) return all edges as pairs of (source, target, direction), i.e. ('U', 'A', 'R')."""
    edges = []
    for i in range(layout.shape[0]):
        for j in range(layout.shape[1]):
            current = np.array((i, j))
            if layout[tuple(current)] is None:
                continue
            for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor = current + np.array(offset)
                if neighbor[0] < 0 or neighbor[0] >= layout.shape[0] or neighbor[1] < 0 or neighbor[1] >= layout.shape[1] or layout[tuple(neighbor)] is None:
                    continue
                edges.append({'source': layout[tuple(current)], 'target': layout[tuple(neighbor)], 'direction': label_dict[offset]})
    return edges


dpad_edges = get_edges(dpad_layout)
numpad_edges = get_edges(numpad_layout)

# dpad1 movement
for d2 in dpad_buttons:
    for n in numpad_buttons:
        for edge_dict in dpad_edges:
            G.add_edge(edge_dict['source'] + d2 + n, edge_dict['target'] + d2 + n, label=edge_dict['direction'])

# dpad2 movement
for n in numpad_buttons:
    for edge_dict in dpad_edges:
        G.add_edge(edge_dict['direction'] + edge_dict['source'] + n, edge_dict['direction'] + edge_dict['target'] + n, label='A')

# numpad movement
for edge_dict in numpad_edges:
    G.add_edge('A' + edge_dict['direction'] + edge_dict['source'], 'A' + edge_dict['direction'] + edge_dict['target'], label='A')

# digit input
for n in numpad_buttons:
    G.add_edge('A' + 'A' + n, n, label='A')


with open('day21\\day21real.txt', 'r') as f:
    raw = f.read()

result = 0
for password in raw.split('\n'):
    inputs_needed = 0
    current_state = 'A'
    for digit in password:
        inputs_needed += nx.shortest_path_length(G, 'AA' + current_state, digit)
        current_state = digit
    result += inputs_needed * int(password[:-1])
print(result)