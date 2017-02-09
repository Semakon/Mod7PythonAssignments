from week1.graph import *
from week1.graph_io import *


def bfs(G: Graph, root: Vertex):
    s = set()
    q = [root]
    while q:
        print(q)
        current = q.pop(0)
        print(q)
        for v in current.neighbours:
            if v not in s:
                s.add(v)
                q.append(v)
    pass


if __name__ == "__main__":
    pass
