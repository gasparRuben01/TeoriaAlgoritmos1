#!/usr/bin/env python
from digraph import *

class Paths(object):
	def __init__(self, digraph, origin, destiny):
		self.source = origin
		self.destiny = destiny
		self.distances = [float('inf')]*digraph.v()
		self.distances[self.source] = 0
		self.edges = [None]*digraph.v()
		self.edges[self.source] = 0

	def distance(self, v):
		"""retorna distancia desde origen a nodo v"""
		return self.distances[v]

	def visited(self, v):
		"""retorna true si v fue visitado"""
		return self.distance(v) < float('inf')

	def edge_to(self, v):
		"""retorna la arista incidente a v, en el path de origin hasta v"""
		return self.edges[v]

	def dst_visited(self):
		"""retorna True si el destino fue visitado"""
		return self.visited(self.destiny)
