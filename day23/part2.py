import networkx as nx

file = "./example1.txt"
file = "./input1.txt"

with open(file) as f:
    G = nx.Graph()

    for c1, c2 in [l.split("-") for l in f.read().splitlines()]:
        G.add_node(c1)
        G.add_node(c2)
        G.add_edge(c1, c2)

    cliques = list(nx.find_cliques(G))
    maxLen = max([len(c) for c in cliques])
    maxClique = list(filter(lambda c: len(c) == maxLen, cliques))[0]


    print(",".join(sorted(maxClique)))