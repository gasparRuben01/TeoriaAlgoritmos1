#!/usr/bin/env python

from knapsack import *
import sys
import time
import gc

class Objeto:
	def __init__(self, key, value, weight, x):
		self.key=key
		self.value=value
		self.weight=weight
		self.x=x
	def get_key(self):
		return self.key
	def get_value(self):
		return self.value
	def get_weight(self):
		return self.weight
	def get_x(self):
		return self.x

global bad_tests
bad_tests=[]
global total_tests
total_tests=0

def print_time(objects, instance_name, n, c):	
	tiempo_inicial=time.time()
	knapsack=KnapsackApprox(c,0.1,objects)
	tiempo=time.time()-tiempo_inicial
	gc.collect()	
	line=';'
	print line.join((str(c),str(tiempo)))
	
cant='xxx'
for i in range(1,len(sys.argv)):
	file=open(sys.argv[i])
	cant_act=sys.argv[i].split('/')[-1].split('_')[2]
	if cant!=cant_act:
		cant=cant_act
		print cant
	line=file.readline()
	while(line):
		instance_name=line.strip()
		n=int(file.readline().strip().split()[1])
		c=int(file.readline().strip().split()[1])
		z=int(file.readline().strip().split()[1])
		tiempo=float(file.readline().strip().split()[1])
		objects=[]
		for j in range(int(n)):
			key,value,weight,x=file.readline().strip().split(",")
			objects.append(Objeto(int(key),int(value),int(weight),int(x)))
		print_time(objects, instance_name, n, c)
		#esta linea tiene el separador de instancias ---
		file.readline()
		#esta en blanco
		file.readline()
		line=file.readline()
	file.close()
