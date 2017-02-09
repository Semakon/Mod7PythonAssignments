from week1.graph import *


def create_graph_path(n):
    G = Graph(False, n)
    verts = G.vertices
    i = 0
    while i < n - 1:
        e = Edge(verts[i], verts[i + 1])
        G.add_edge(e)
        i += 1
    return G


def create_graph_cycle(n):
    G = create_graph_path(n)
    e = Edge(G.vertices[n - 1], G.vertices[0])
    G.add_edge(e)
    return G


def create_graph_complete(n):
    G = Graph(False, n, True)
    for u in G.vertices:
        for v in G.vertices:
            if u != v and not u.is_adjacent(v):
                G.add_edge(Edge(u, v))
    return G


# create_graph_path test
n = 10
# path = create_graph_path(n)
# print(path)
# print(len(path.edges) == n - 1 and len(path.vertices) == n)
#
#
# # create_graph_cycle test
# cycle = create_graph_cycle(n)
# print(cycle)
# print(len(cycle.edges) == n and len(cycle.vertices) == n)
#
#
# # create_graph_complete test
# comp = create_graph_complete(n)
# print(comp)
# print(len(comp.edges) == (n * (n - 1)) // 2 and len(comp.vertices) == n)


# test Graph.__add__
G = create_graph_path(n)
H = create_graph_path(n)
print("\nG:\n" + str(G))
print("\nH:\n" + str(H))
print("\nG + H:\n" + str(G + H))
