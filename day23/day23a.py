import networkx as nx

with open('day23\\day23real.txt', 'r') as f:
    raw = f.read()

G = nx.Graph()

for line in raw.split('\n'):
    a = line.split('-')[0]
    b = line.split('-')[1]
    assert a != b
    G.add_node(a)
    G.add_node(b)
    G.add_edge(a, b)

assert len(G.edges) == len(raw.split('\n'))


triangles = []

for u in G.nodes:
    for n1 in nx.all_neighbors(G, u):
        for n2 in nx.all_neighbors(G, u):
            if n2 in G.neighbors(n1):
                if u[0] == 't' or n1[0] == 't' or n2[0] == 't':
                    triangles.append(tuple(sorted((u, n1, n2))))

print(len(set(triangles)))