from sys import *
from bhk import *
from time import *

def read_file(name_file):
    to_read = open(name_file)
    matrix = []
    for line in to_read:
        line = line.split(" ")
        line = [int(value) for value in line]
        matrix.append(line[:])

    to_read.close()
    return matrix

def print_result(delta_time, N, cost, path):
	str_time = str(delta_time)
	str_N = str(N)
	str_cost = str(cost)
	str_path = [str(v) for v in path]
	sep = "-"
	str_path = sep.join(str_path) 
	sep = ","
	str_result = sep.join([str_time, str_N, str_cost, str_path])
	print str_result

def test_tsp(G, N):
	init = time()
	cost, path = bhk(G, N)
	delta_time = time() - init
	print_result(delta_time, N, cost, path)

size_graph = [4,15,17,26,42,48]
print "time,size,cost_min,path_min"
for N in size_graph:
	name_file = "graph_" + str(N) + "_vertex.txt"
	G = read_file(name_file)
	test_tsp(G, N)


