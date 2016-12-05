from digraph import *

def tsp_aprox(G, N):
    root = 0
    path, c = [], 0
    MST = G.mst_prim(root)
    MST.pre_order(root, path)
    path.append(root)
    for i in range(N):
        c += G.weigth(path[i], path[i+1])

    return c, path
