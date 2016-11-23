#!/usr/bin/env python

from Knapsack import *
import sys
import time

class Objeto:
	def __init__(self, key, value, weigth, x):
		self.key=key
		self.value=value
		self.weigth=weigth
		self.x=x
	def get_key(self):
		return self.key
	def get_value(self):
		return self.value
	def get_weigth(self):
		return self.weigth
	def get_x(self):
		return self.x

global bad_tests
bad_tests=[]
global total_tests
total_tests=0

def print_time(objects, instance_name, n, c):	
	tiempo_inicial=time.time()
	knapsack=Knapsack(c,objects)
	tiempo=time.time()-tiempo_inicial	
	line=';'
	print line.join((instance_name, str(n), str(c),str(tiempo)))
	

for i in range(1,len(sys.argv)):
	file=open(sys.argv[i])
	print "Archivo: "+sys.argv[i]
	line=file.readline()
	while(line):
		instance_name=line.strip()
		n=int(file.readline().strip().split()[1])
		c=int(file.readline().strip().split()[1])
		z=int(file.readline().strip().split()[1])
		tiempo=float(file.readline().strip().split()[1])
		objects=[]
		for j in range(int(n)):
			key,value,weigth,x=file.readline().strip().split(",")
			objects.append(Objeto(int(key),int(value),int(weigth),int(x)))
		print_time(objects, instance_name, n, c)
		#esta linea tiene el separador de instancias ---
		file.readline()
		#esta en blanco
		file.readline()
		line=file.readline()
	file.close()
