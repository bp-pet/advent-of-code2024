"""
Record all possible paths between each two buttons. Choose one to use always based on the heuristic of button priority. No combination of priorities gives the right result.
"""
# Step 1: record paths between buttons

import numpy as np
import networkx as nx

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

# Step 2: choose sequences to use

def rate_seq(seq, primary_button, secondary_button):
    """Get a score for a sequence based on positions of two buttons."""
    return sum([pos for pos, char in enumerate(seq) if char == primary_button]) + 0.1 * sum([pos for pos, char in enumerate(seq) if char == secondary_button])

def choose_sequence(list_of_seq, primary_button, secondary_button):
    """Get the sequence with the lowest score."""
    return sorted(list_of_seq, key=lambda x: rate_seq(x, primary_button, secondary_button))[0]


directions = ('U', 'D', 'L', 'R')
combinations = []
for d1 in directions:
    for d2 in directions:
        for d3 in directions:
            for d4 in directions:
                combinations.append((d1, d2, d3, d4))

class Pad:
    def __init__(self, pad_type: str):
        self.current_position = 'A'
        if pad_type == 'num':
            self.sequences = numpad_sequences
        elif pad_type == 'dir':
            self.sequences = dpad_sequences
        else:
            raise Exception('Type of pad not implemented')
    
    def press_key(self, key_to_press):
        """Returns all (shortest) sequences of keys that can get to new state (and press it) and sets new state."""
        sequence_key = self.current_position + key_to_press
        self.current_position = key_to_press
        try:
            return self.sequences[sequence_key]
        except KeyError:
            raise Exception('Something is wrong')


for combination in combinations:

    numpad_sequences = {}
    for k in numpad_sequences_options:
        numpad_sequences[k] = choose_sequence(numpad_sequences_options[k], combination[0], combination[1])

    dpad_sequences = {}
    for k in dpad_sequences_options:
        dpad_sequences[k] = choose_sequence(dpad_sequences_options[k], combination[2], combination[3])



    numpad = Pad('num')
    dpad1 = Pad('dir')
    dpad2 = Pad('dir')

    with open('day21\\day21example.txt', 'r') as f:
        raw = f.read()
    passwords = raw.split('\n')

    result = 0
    for password in passwords:
        required_sequence = ''
        for c0 in password:
            for c1 in numpad.press_key(c0):
                for c2 in dpad1.press_key(c1):
                    required_sequence += dpad2.press_key(c2)
        result += len(required_sequence) * int(password[:-1])
    if result < 127000:
        print(result)