import numpy as np
import networkx as nx

dpads_count = 25

dpad_buttons = ['L', 'R', 'U', 'D', 'A']
numpad_buttons = [str(i) for i in range(10)] + ['A']

numpad_layout = np.array([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']])
dpad_layout = np.array([[None, 'U', 'A'], ['L', 'D', 'R']])

label_dict = {(1, 0): 'D', (-1, 0): 'U', (0, 1): 'R', (0, -1): 'L'}

def path_nodes_to_edges(G, path):
    """Given a graph and a path made of nodes, return a string of concatenated edge labels + 'A' in the end."""
    edge_path = ''
    for i in range(len(path) - 1):
        edge_path += G.edges[path[i], path[i + 1]]['label']
    return edge_path + 'A'

def layout_to_graph(layout):
    """From a layout make the same graph."""
    G = nx.DiGraph()
    for i in range(layout.shape[0]):
        for j in range(layout.shape[1]):
            current = np.array((i, j))
            if layout[tuple(current)] is None:
                continue
            for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor = current + np.array(offset)
                if neighbor[0] < 0 or neighbor[0] >= layout.shape[0] or neighbor[1] < 0 or neighbor[1] >= layout.shape[1] or layout[tuple(neighbor)] is None:
                    continue
                G.add_node(layout[tuple(current)])
                G.add_node(layout[tuple(neighbor)])
                G.add_edge(layout[tuple(current)], layout[tuple(neighbor)], label=label_dict[offset])
    return G

def graph_to_sequences(G):
    """From a graph get all sequences/paths for each pair of nodes."""
    sequences = {}
    for n1 in G.nodes:
        for n2 in G.nodes:
            sequences[n1 + n2] = [path_nodes_to_edges(G, path) for path in nx.all_shortest_paths(G, n1, n2)]
    return sequences

numpad_sequences_options = graph_to_sequences(layout_to_graph(numpad_layout))
dpad_sequences_options = graph_to_sequences(layout_to_graph(dpad_layout))

lookup = {}

def calculate_steps(level, start, target):
    if (level, start, target) in lookup:
        return lookup[(level, start, target)]
    paths = dpad_sequences_options[start + target] if level < dpads_count else numpad_sequences_options[start + target]
    value_per_path = {}
    if level == 0:
        result = len(paths[0])
    else:
        for path in paths:
            min_presses = 0
            current = 'A'
            for button in path:
                min_presses += calculate_steps(level - 1, current, button)
                current = button
            value_per_path[path] = min_presses
        result = min(value_per_path.values())
    lookup[(level, start, target)] = result
    return result


with open('day21\\day21real.txt', 'r') as f:
    raw = f.read()
passwords = raw.split('\n')

result = 0
for password in passwords:
    current = 'A'
    value = 0
    for c in password:
        value += calculate_steps(dpads_count, current, c)
        current = c
    result += value * int(password[:-1])

print(result)