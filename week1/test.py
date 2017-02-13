from week1.graph_io import *

with open('data\\weightedexample.gr') as f:
    G = load_graph(f)
with open('data\\mygraph.dot', 'w') as f:
    write_dot(G, f)
