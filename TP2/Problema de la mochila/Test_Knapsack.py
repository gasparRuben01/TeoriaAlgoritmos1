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

def test_instance(objects, instance_name, n, c, z, tiempo):
	print "###########" + str(len(objects))	
	global total_tests
	global bad_tests
	total_tests+=1
	tiempo_inicial=time.time()
	knapsack=Knapsack(c, objects)
	tiempo_usado=time.time()-tiempo_inicial
	missing_elements=[]
	wrong_elements=[]
	for i in objects:
		if i.get_x()==1:
			if not i in knapsack.get_elements(): missing_elements.append(i)
		else:
			if i in knapsack.get_elements(): wrong_elements.append(i)
	if tiempo_usado>tiempo or knapsack.get_value()!=z or len(missing_elements)!=0 or len(wrong_elements)!=0:
		bad_tests.append(instance_name)
		print "Prueba Erronea #####"

	print  "Prueba" + instance_name + " :"
	print "tiempo time:"+str(tiempo)+" tiempo que tomo:"+str(tiempo_usado)
	print "valor z:"+str(z)+" valor obtenido:"+str(z)
	if len(missing_elements)!=0:
		print "elementos faltantes en la bolsa:"+str(len(missing_elements))
		for j in missing_elements:
			print "----"+str(j.get_key())
	if len(wrong_elements)!=0:
		print "elementos que no deberian estar:"+str(len(wrong_elements))
		for j in missing_elements:
			print "----"+str(j.get_key())
	print "\n"*2
	


for i in range(1,len(sys.argv)):
	file=open(sys.argv[i])
	print "archivo "+sys.argv[i]
	print "\n"
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
		test_instance(objects, instance_name, n, c, z, tiempo)
		#esta linea tiene el separador de instancias ---
		file.readline()
		#esta en blanco
		file.readline()
		line=file.readline()

	print "Total pruebas:"+str(total_tests)
	print "Bad tests:"+str(len(bad_tests))
	for i in bad_tests:
		print "----"+i
	print "Good tests:"+str(total_tests-len(bad_tests))
	print "\n"
	total_tests=0
	bad_tests=[]
