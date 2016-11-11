from sys import *
from bhk import *

def read_file(name_file, N):
    to_read = open(name_file)
    matrix = []
    for line in to_read:
        line = line.split(" ")
        line = [int(value) for value in line]
        matrix.append(line[:])

    to_read.close()
    return matrix

name_file, N = argv[1], int(argv[2])
G = read_file(name_file, N)
cost, path = bhk(G, N)
print cost
print path
