import random
import time
import sys
import importlib
from fuerza_bruta import *
from heap_select import *
from k_heapsort import *
from k_selection import *
from quick_select import *
from sorted_selection import *

def list_test(name):
	to_read = open(name)
	elements = []
	for i in to_read:
		elements.append(int(i))

	to_read.close()
	return elements

elements = list_test(sys.argv[1])
n = len(elements)
k = 25000
orders = {"fuerza bruta":fuerza_bruta, "heap select":heap_select,"k_heapsort":k_heapsort,"k_selection":k_selection,"quick_select":quick_select,"sorted_selection":sorted_selection}

for order in orders.keys():
	order_k = orders[order]
	print order
	result = order_k(elements[:], k)
	print order + " con " + str(k) + " resulto " + str(result)
