#!/usr/bin/env python

class Paths(object):
	def __init__(self, digraph, origin_node):
		self.source=origin_node

	def distance(self, v):
		"""retorna distancia desde origen a nodo v"""
		raise NotImplementedError("Abstrcat class")

	def visistado(v):
		"""retorna true si v fue visitado"""
		return distancia(v)<float('inf')

	def path(v):
		"""retorna uno de los caminos mas cortos a v, partiendo del origen"""
		raise NotImplementedError("Abstract class")
