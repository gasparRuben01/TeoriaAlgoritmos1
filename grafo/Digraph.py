#!/usr/bin/env python

class Digraph(object):
	def __init__(self, v):
		"""Construye un digrafo sin aristas de v vertices"""
		self.vertexs=[]
		for i in range(v):
			self.vertexs.append([])

	def v(self):
		return len(self.vertexs)
	
	def add_edge(self, u, v, weigth=0):
		"""Agrega una arista con peso weigth al grafo. Su cola es u y la cabeza v"""		
		self.vertexs[u].append((u, v, weigth))
	
	def adj_e(self, v):
		"""Retorna iterador de las aristas adyacentes a v"""
		return self.vertexs[v].__iter__()

	def __iter__(self):
		return iter(range(self.v()))
