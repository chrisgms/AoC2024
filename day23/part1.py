import networkx as nx

file = "./example1.txt"
file = "./input1.txt"

with open(file) as f:
    G = nx.Graph()

    for c1, c2 in [l.split("-") for l in f.read().splitlines()]:
        G.add_node(c1)
        G.add_node(c2)
        G.add_edge(c1, c2)

    clique3 = filter(lambda c: len(c) == 3, nx.enumerate_all_cliques(G))
    
    count = 0
    for (a, b, c) in clique3:
        if a[0] == "t" or b[0] == "t" or c[0] == "t": count += 1

    print(count)