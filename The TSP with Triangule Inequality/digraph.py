#!/usr/bin/env python
from pqueue import *

class Edge(object):
    """docstring for Edge."""
    def __init__(self, src, dst, weigth):
        super(Edge, self).__init__()
        self.src = src
        self.dst = dst
        self.weigth = weigth

class Digraph(object):
	def __init__(self, v):
		"""Construye un digrafo sin aristas de v vertices"""
		self.vertexs = []
		self.edges = []
		for i in range(v):
			self.vertexs.append({})

	def v(self):
		#cantidad de verices
		return len(self.vertexs)

	def e(self):
		#cantidad de aristas
		return len(self.edges)

	def add_edge(self, u, v, weigth = 0):
		#agregamos una arista
		e = Edge(u, v, weigth)
		self.vertexs[u][v] = e
		self.edges.append(e)

	def adj_e(self, v):
		#lista de aristas adjacentes a v
		return self.vertexs[v].values()

	def __iter__(self):
		return iter(range(self.v()))

	def adj(self, v):
		#lista de vertices adjacentes a v
		return self.vertexs[v].keys()

	def iter_edges(self):
		#lista de aristas del grafo
		return self.edges

	def weigth(self, u, v):
		return self.vertexs[u][v].weigth

	def mst_prim(self, root):
		mst = Digraph(len(self.vertexs))
		dad = [None] * len(self.vertexs)
		pqueue = PQueue()
		for i in range(len(self.vertexs)):
			pqueue.push(float('Inf'), i)

		pqueue[root] = 0
		while not pqueue.empty():
			u = pqueue.pop()
			for e in self.adj_e(u):
				if e.dst in pqueue and e.weigth < pqueue[e.dst]:
					pqueue[e.dst] = e.weigth
					dad[e.dst] = e.src

		for i in range(1, len(self.vertexs)):
			mst.add_edge(dad[i], i, self.weigth(dad[i], i))

		return mst

	def pre_order(self, u, order):
		order.append(u)
		pqueue = PQueue()
		for e in self.adj_e(u):
			pqueue.push(e.weigth, e.dst)

		while not pqueue.empty():
			v = pqueue.pop()
			self.pre_order(v, order)