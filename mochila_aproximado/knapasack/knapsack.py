#!/usr/bin/env python
from math import ceil

class ObjetoWrapper(object):
	def __init__(self,objeto,nuevo_valor):
		self.objeto=objeto
		self.value=nuevo_valor
	def get_value(self):
		return self.value
	def get_weight(self):
		return self.objeto.get_weight()
	def get_objeto(self):
		return self.objeto

class Knapsack(object):
	def fill(self,objetos,sum_values,matrix):
		i=len(matrix)-1
		v=self.value
		while i>0 and v>0:
			k=i-1
			if v>sum_values[k] or matrix[i-1][max(0,v-objetos[k].get_value())]<matrix[i-1][v]:
				self.elements.append(objetos[k])
				v-=objetos[k].get_value()
			i-=1

	def __init__(self,capacity,objetos):
		self.capacity=capacity
		#en la posicion i de este array se guarda la suma de los valores de los elementos que se encuentran en posiciones menores a i.
		sum_values=[0]*(len(objetos)+1)
		for i in range(1,len(sum_values)):
			sum_values[i]=objetos[i-1].get_value()+sum_values[i-1]
		rows=len(objetos)+1
		columns=sum_values[-1]
		matrix=[[0]*columns for i in range(rows)]
		for i in range(1,rows):
			k=i-1
			for v in range(1,columns):
				if v>sum_values[k]:
					matrix[i][v]=objetos[k].get_weight()+matrix[i-1][max(0,v-objetos[k].get_value())]
				else:
					matrix[i][v]=min(matrix[i-1][v],matrix[i-1][max(0,v-objetos[k].get_value())])

		for v in reversed(range(0,columns)):
			if matrix[-1][v]<=self.capacity:
				self.value=v
				break
		self.elements=[]
		self.fill(objetos,sum_values,matrix)
		
	def get_value(self):
		return self.value
	def get_elements(self):
		return self.elements
	def get_capacity(self):
		return self.capacity

class KnapsackApprox(Knapsack):
	def __init__(self, capacity, error, objetos):
		self.capacity=capacity
		self.error=error
		max_value=max([i.get_value() for i in objetos])
		b=(error/(2*len(objetos)))*max_value
		objetos_escalados=[ObjetoWrapper(i,int(ceil(i.get_value()/b))) for i in objetos]
		knapsack=Knapsack(capacity,objetos_escalados)
		self.elements=[i.get_objeto() for i in knapsack.get_elements()]
		self.value=0
		for i in knapsack.get_elements(): self.value+=i.get_value()

if __name__=='__main__':

	class Objeto(object):
		def __init__(self,v,w):
			self.v=v
			self.w=w
		def get_value(self):
			return self.v
		def get_weight(self):
			return self.w

	a=[Objeto(2,1),Objeto(3,4),Objeto(3,1)]
	b=Knapsack_approx(5,1/100.,a)
