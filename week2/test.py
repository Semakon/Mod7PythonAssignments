import math

from week2.heap import Heap
from week1.graph import *


# Initializing test variables
G = Graph(False, 15)
E = G.vertices
for v in E:
    v.dist = math.inf
v, *remainder = E
v.dist = 0
Q = Heap(E, False)

# Starting tests
print(G)
print(Q)

Q.insert(Vertex(G))
print(Q)

# TODO: fix heap.py (v.dist must be set for it to be recognized)
