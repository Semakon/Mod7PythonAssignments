from week1.graph_io import load_graph, save_graph, write_dot
from week1.graph import *


def complement(filename):
    with open('data\\' + filename) as f:
        G = load_graph(f)
    print(G)
    H = Graph(G.directed)
    temp = dict()
    for v in G.vertices:
        newV = Vertex(H)
        H.add_vertex(newV)
        temp[v] = newV
    i = 0
    while i < len(G.vertices):
        j = i + 1
        while j < len(G.vertices):
            u = G.vertices[i]
            v = G.vertices[j]
            if u != v and not G.find_edge(u, v):
                H.add_edge(Edge(temp[u], temp[v]))
            j += 1
        i += 1
    with open('data\\newgraph', 'w') as f:
        save_graph(H, f)
    return H

# complement of examplegraph.gr
# print(complement("examplegraph.gr"))
graph = Graph(False, 5)
u, v, w, *remainder = graph.vertices
graph.add_edge(Edge(u, v))
graph.add_edge(Edge(v, w))
graph.add_edge(Edge(u, w))
with open('data\\examplegraph2.gr', 'w') as f:
    save_graph(graph, f)
graph2 = complement('examplegraph2.gr')

with open('data\\tsjak.dot', 'w') as f:
    write_dot(graph2, f)
