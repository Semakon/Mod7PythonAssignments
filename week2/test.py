import math
from random import randint

from week2.heap import Heap
from week1.graph import *


# Initializing test variables
n = 6
G = Graph(False, n)
E = G.vertices
for i in range(0, len(E) - 1, 2):
    E[i].dist = math.inf
    E[i+1].dist = randint(0, n)
Q = Heap(E, False)
# Starting tests
for v in E:
    print(v.__str__() + ": " + str(v.dist))
print(Q)

# while Q.is_not_empty():
#
#     u = Q.top
#     Q.delete(u)
#     print("\n" + str(Q))
#     print(u.__str__() + ": " + str(u.dist))

u = Q.top
Q.delete(u)
print("\n" + str(Q))
print(u.__str__() + ": " + str(u.dist))
u = Q.top
Q.delete(u)
print("\n" + str(Q))
print(u.__str__() + ": " + str(u.dist))
u = Q.top
Q.delete(u)
print("\n" + str(Q))
print(u.__str__() + ": " + str(u.dist))
