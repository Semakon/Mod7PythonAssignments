from week1.graph_io import write_dot, load_graph
from week1.graph import *


with open('data\\examplegraph2.gr') as f:
    G = load_graph(f)
with open('data\\mygraph.dot', 'w') as f:
    write_dot(G, f)
