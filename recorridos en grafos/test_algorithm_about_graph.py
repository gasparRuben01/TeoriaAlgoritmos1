from bfs import *
from dijkstra import *
from sbh import *
from digraph import *
from a_star import *
from sys import *
from edge import *

def read_file(name, n):
	G = Digraph(n)
	toRead = open(name)
	for row in toRead:
		r = row[:-3]
		rs = r.split('	')
		v = int(rs[0])
		for i in rs[1:]:
			isp = i.split(',')
			w = int(isp[0])
			l = int(isp[1])
			G.add_edge(v-1, w-1, l)

	toRead.close()
	return G

def print_result(algstr,dst,alg):
    print algstr + "," + str(dst) + "," + str(alg.distance(dst)) + "," + str(alg.edge_to(dst))

digraph = read_file(argv[1], int(argv[2]))
heuristic = []
sample = [6,36,58,81,98,114,132,164,187,196]
for i in range(int(argv[2])):
    heuristic.append({})
    for j in sample:
        dijkstra = Dijkstra(digraph, i, j)
        heuristic[i][j] = dijkstra.distance(j)

print "alghorithm,destino,long_path,path"
for d in sample:
	h = lambda v:  heuristic[v][d]
	dijkstra = Dijkstra(digraph, 0, d)
	bfs = BFS(digraph, 0, d)
	sbh = SBH(digraph, 0, d, h)
	astar = AStar(digraph, 0, d, h)
	print_result("dijkstra",d,dijkstra)
	print_result("bfs",d,bfs)
	print_result("sbh",d,sbh)
	print_result("AStar",d,astar)
