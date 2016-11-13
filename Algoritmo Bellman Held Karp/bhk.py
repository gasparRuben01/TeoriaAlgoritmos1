from struct_bhk import *
from itertools import *

# genera un par (c, v) donde c es el menor 
# costo de los calculados y v es el vertice
# previo a x
def min_cost(G, C, s, x):
    s_x = tuple(i for i in s if i != x)
    return min([(C[s_x, m][0] + G[m][x], m) for m in s_x])

# genera el circuito de hammilton cuyo costo 
# es minimo
def min_path(C, s, p):
    sset = set(s)
    path = [0]
    while p != 0:
        path.append(p)
        q = C[sset, p][1]
        sset.remove(p)
        p = q

    path.append(0)
    path.reverse()
    return path

def bhk(G, N):
    C = StructBHK()
    for k in range(1,N):
        C[[k], k] = G[0][k], 0

    for size in range(2,N):
        for s in combinations(range(1, N), size):
            for x in s:
                C[s, x] = min_cost(G, C, s, x)

    s = range(N)
    (c, p) = min_cost(G, C, s, 0)
    s = range(1, N)
    path = min_path(C, s, p)
    return c, path
