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

cliques = nx.find_cliques(G)
max_clique = max(list(cliques), key=len)
result = ','.join(sorted(max_clique))
print(result)