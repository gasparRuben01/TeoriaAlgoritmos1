#!/usr/bin/env python
from edge import *
from pqueue import *

class Digraph(object):
	def __init__(self, v):
		"""Construye un digrafo sin aristas de v vertices"""
		self.vertexs = []
		self.edges = []
		for i in range(v):
			self.vertexs.append(([], []))
		self.EADJ = 0
		self.VADJ = 1

	def v(self):
		#cantidad de verices
		return len(self.vertexs)

	def e(self):
		#cantidad de aristas
		return len(self.edges)

	def add_edge(self, u, v, weigth = 0):
		#agregamos una arista
		e = Edge(u, v, weigth)
		self.vertexs[u][self.EADJ].append(e)
		self.vertexs[u][self.VADJ].append(v)
		self.edges.append(e)

	def adj_e(self, v):
		#lista de aristas adjacentes a v
		return self.vertexs[v][self.EADJ]

	def __iter__(self):
		return iter(range(self.v()))

	def adj(self, v):
		#lista de vertices adjacentes a v
		return self.vertexs[v][self.VADJ]

	def iter_edges(self):
		#lista de aristas del grafo
		return self.edges

	def mst_prim(self):
		mst = Digraph(len(self.vertexs))
		pqueue = PQueue()
		for i in range(len(self.vertexs)):
			pqueue.push(float('Inf'), i)

		pqueue[0] = 0
		while not pqueue.empty():
			u = pqueue.pop()
			for e in self.vertexs[u][self.EADJ]:
				if e.dst in pqueue and e.weigth < pqueue[e.dst]:
					pqueue[e.dst] = e.weigth
					mst.add_edge(e.src, e.dst, e.weigth)

		return mst
