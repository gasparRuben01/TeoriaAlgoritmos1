#!/usr/bin/python
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

def medir(orden_k, elements, k):
	tiempo_inicial = time.time()
	orden_k(elements, k)
	return time.time()-tiempo_inicial

def list_test(name):
	to_read = open(name)
	elements = []
	for i in to_read:
		elements.append(int(i))

	to_read.close()
	return elements

elements = list_test(sys.argv[1])
print "list of integer ready"
orders = {"fuerza bruta":fuerza_bruta, 
"heap select":heap_select,
"k_heapsort":k_heapsort,
"k_selection":k_selection,
"quick_select":quick_select,
"sorted_selection":sorted_selection}
print "orders ready"
n = len(elements)
ks = [0, n/2, n-1]

print "order,k,time"
for order in orders.keys():
	for k in ks:
		time_exec = medir(orders[order], elements[:], k)
		print order + "," + str(k) + "," + str(time_exec)
