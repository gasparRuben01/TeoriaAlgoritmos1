from cost_path import *
from itertools import *

# generar sub conjuntos de tamanio M
# de un conjunto [n,N -1)
def subsets(n, N, M):
    subset = combinations(range(n, N), M)
    subset = [list(s) for s in subset]
    return subset

def min_cost(G, C, s, x):
    s_x = s[:]
    s_x.remove(x)
    return min([(C[s_x, m][0] + G[m][x], m) for m in s_x])


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
    C = CostPath()
    for k in range(1,N):
        C[[k], k] = G[0][k], 0

    for size in range(2,N):
        for s in subsets(1, N, size):
            for x in s:
                C[s, x] = min_cost(G, C, s, x)

    s = range(N)
    (c, p) = min_cost(G, C, s, 0)
    s = range(1, N)
    path = min_path(C, s, p)
    return c, path
