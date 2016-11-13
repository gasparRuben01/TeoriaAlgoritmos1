from Knapsack import *
import sys
import time

class Objeto:
	def __init__(self, key, value, weight, x):
		self.key=key
		self.value=value
		self.weight=weight
		self.x=x
	def get_key():
		return self.key
	def get_value():
		return self.value
	def get_weight():
		return self.weight
	def get_x():
		return self.x

bad_tests=[]
total_tests=0

def test_instance(objects, instance_name, n, c, z, time):
	total_test+=1
	tiempo_inicial=time.time()
	knapsack=knapsack(c, objects)
	tiempo=time.time()-tiempo_inicial
	instance_name=instance_name
	missing_elements=[]
	wrong_elements=[]
	for i in objects:
		if objects.get_x()==1:
			if not i in knapsack.get_elements(): missing_elements.append(i)
		else:
			if i in knapsack.get_elements(): wrong_elements.append(i)
	if tiempo>time or knapsack.get_value()!=z or len(missing_elements)!=0 or len(wrong_elements)!=0:
		bad_tests.append(instance_name)
		print "Prueba Erronea #####"
	print "Prueba " str(instance_name)":"
	print "tiempo time:"str(c)" tiempo que tomo:"str(tiempo)
	print "valor z:"str(z)" valor obtenido:"str(z)
	if len(missing_elemnts)!=0:
		print "elementos faltantes es la bolsa:"
		for j in missing_elements:
			print "----"str(j.get_key())
	if len(wrong_elemnts)!=0:
		print "elementos que no deberian estar:"
		for j in missing_elements:
			print "----"str(j.get_key())
	print "\n"*2
	


for i in range(1, len(sys.argv)):
	file=open(sys.argv[i])
	objects=[]
	print "archivo "sys.argv[i]
	print "\n"
	for line in file:
		instance_name=line.strip().split()[1]
		n=file.readline().strip().split()[1]
		c=file.readline().strip().split()[1]
		z=file.readline().strip().split()[1]
		time=file.readline().strip().split().[1]
		for j in range(n):
			key,value,weight,x=file.readline().strip().split(",")
			objects.append(Objeto(key,value,weight,x))
			test_instance(objects, instance_name, n, c, z, time)
		#esta linea tiene el separador de instancias ---
		file.readline()
		#esta un espacio en blanco
		file.readline()
	print "Total pruebas:"str(total_tests)
	print "Bad tests:"str(len(bad_tests))
	print "Good tests:"str(total_test-len(bad_tests))
	print "\n"
	total_tests=0
	bad_tests=[]
