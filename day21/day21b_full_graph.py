"""
Doesn't work due to graph being too large.
"""
import numpy as np
import networkx as nx
import itertools

dpads_count = 2

dpad_buttons = ['L', 'R', 'U', 'D', 'A']
numpad_buttons = [str(i) for i in range(10)] + ['A']

numpad_layout = np.array([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']])
dpad_layout = np.array([[None, 'U', 'A'], ['L', 'D', 'R']])

label_dict = {(1, 0): 'D', (-1, 0): 'U', (0, 1): 'R', (0, -1): 'L'}

G = nx.DiGraph()

states = []
for s in list(itertools.product(dpad_buttons, repeat=dpads_count)):
    for n in numpad_buttons:
        states.append(''.join(s) + n)
for state in states:
    G.add_node(state)


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


def add_edges(index):
    assert index >= 0 and index <= dpads_count

    prefix = 'A' * (index - 1)
    suffixes = []
    if index < dpads_count:
        for s in list(itertools.product(dpad_buttons, repeat=(dpads_count - index - 1))):
            for n in numpad_buttons:
                suffixes.append(''.join(s) + n)
    else:
        suffixes = ['']

    layout = dpad_layout if index < dpads_count else numpad_layout
    for i in range(layout.shape[0]):
        for j in range(layout.shape[1]):
            current = np.array((i, j))
            if layout[tuple(current)] is None:
                continue
            for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor = current + np.array(offset)
                if neighbor[0] < 0 or neighbor[0] >= layout.shape[0] or neighbor[1] < 0 or neighbor[1] >= layout.shape[1] or layout[tuple(neighbor)] is None:
                    continue
                for suffix in suffixes:
                    if index > 0:
                        G.add_edge(
                            prefix + label_dict[offset] + layout[tuple(current)] + suffix,
                            prefix + label_dict[offset] + layout[tuple(neighbor)] + suffix,
                            label='A')
                    else:
                        G.add_edge(layout[tuple(current)] + suffix, layout[tuple(neighbor)] + suffix, label=label_dict[offset])

for i in range(dpads_count + 1):
    add_edges(i)

# add exit nodes
for n in numpad_buttons:
    G.add_edge(('A' * dpads_count) + n, n, label='A')


with open('day21\\day21real.txt', 'r') as f:
    raw = f.read()

result = 0
for password in raw.split('\n'):
    inputs_needed = 0
    current_state = 'A'
    for digit in password:
        inputs_needed += nx.shortest_path_length(G, ('A' * dpads_count) + current_state, digit)
        current_state = digit
    result += inputs_needed * int(password[:-1])
print(result)