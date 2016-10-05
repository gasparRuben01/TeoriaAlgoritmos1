#!/usr/bin/env python

class Paths(object):
	def __init__(self, digraph, origin_node):
		self.source=origin_node
		self.distances=[float('inf')]*digraph.v()
		self.edges=[None]*digraph.v()

	def distance(self, v):
		"""retorna distancia desde origen a nodo v"""
		return self.distances[v]

	def visitado(v):
		"""retorna true si v fue visitado"""
		return distancia(v)<float('inf')

	def path(v):
		"""retorna uno de los caminos mas cortos a v, partiendo del origen
		   Si v es el origen retorna una lista vacia, si v no es alcanzable desde origen lanza
	           lanza exception"""
		if not visitado(v):
			raise ValueError("vertice no alcanzable desde origen")
		stack=[]
		while self.edges[v]:
			stack.append(self.edges[v])
			v=self.edges[v][0]
		return stack
	
	def edge_to(v):
		"""retorna la arista incidente a v, en el path de origin hasta v. si v no es alcanzable desde origen lanza exception"""
		if not visitado(v):
			raise ValueError("vertice no alcanzable desde origen")
		return self.edges(v)
