from digraph import *
from tsp_aprox import *
from sys import *
from time import *

def read_file(name_file):
    matrix = []
    with open(name_file, "rb") as graph_file:
        for line in graph_file:
            line = line.split(" ")
            line = [int(v) for v in line]
            matrix.append(line[:])

    G = Digraph(len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            G.add_edge(i, j, matrix[i][j])

    return G

def print_result(delta_time, N, cost, path):
	str_time = str(delta_time)
	str_N = str(N)
	str_cost = str(cost)
	str_path = [str(v+1) for v in path]
	sep = "-"
	str_path = sep.join(str_path)
	sep = ","
	str_result = sep.join([str_time, str_N, str_cost, str_path])
	print str_result

def test_tsp(G, N):
	init = time()
	cost, path = tsp_aprox(G, N)
	delta_time = time() - init
	print_result(delta_time, N, cost, path)

# -a construye grafos de los archivos segun tamanio
# pasado por parametro, ej: test_bhk.py -a 4 15
# busca los archivos cuyos grafos son de tamanio 4 y 15

#-t construye sub grafos del archivo "graph_26_vertex.txt"
# de tamanios [4, n] siendo n un parametro
# ej: test_bhk.py -t 20
# construye subgrafos de tamanio [4 - 20]
print "time,size,cost_min,path_min"
if argv[1] == "-a":
	size_graph = argv[2:]
	for N in size_graph:
		N = int(N)
		name_file = "graph_" + str(N) + "_vertex.txt"
		G = read_file(name_file)
		test_tsp(G, N)

if argv[1] == "-t":
	name_file = "graph_48_vertex.txt"
	G = read_file(name_file)
	for N in range(4, int(argv[2])):
		test_tsp(G, N)
