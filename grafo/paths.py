#!/usr/bin/env python
import digraph

class Paths(object):
	def __init__(self, digraph, origin_node):
		self.source=origin_node
		self.distances=[float('inf')]*digraph.v()
		self.edges=[None]*digraph.v()

	def distance(self, v):
		"""retorna distancia desde origen a nodo v"""
		return self.distances[v]

	def visitado(self,v):
		"""retorna true si v fue visitado"""
		return self.distance(v)<float('inf')

	def path(self, v):
		"""retorna uno de los caminos mas cortos a v, partiendo del origen
		   Si v es el origen retorna una lista vacia, si v no es alcanzable desde origen lanza
	           lanza exception"""
		if not self.visitado(v):
			raise ValueError("vertice no alcanzable desde origen")
		path=[]
		while self.edges[v]:
			path.insert(0, self.edges[v])
			v=self.edges[v][0]
		return path
	
	def edge_to(self, v):
		"""retorna la arista incidente a v, en el path de origin hasta v. si v no es alcanzable desde origen lanza exception"""
		if not visitado(v):
			raise ValueError("vertice no alcanzable desde origen")
		return self.edges(v)
