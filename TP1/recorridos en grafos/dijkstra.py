#!/usr/bin/env python
from paths import *
from digraph import *
from pqueue import *
from edge import *

class Dijkstra(Paths):
	"""docstring for Dijkstra."""
	def __init__(self, digraph, origin, destiny, heuristic = lambda v: 0):
		super(Dijkstra, self).__init__(digraph, origin, destiny)
		pqueue = PQueue()

		for e in digraph.adj_e(origin):
			pqueue.push(self.distances[origin] + e.weigth, e)

		while not pqueue.empty():
			e = pqueue.pop()
			if self.visited(e.dst): continue

			self.distances[e.dst] = self.distances[e.src] + e.weigth
			self.edges[e.dst] = e.src
			if self.dst_visited(): break

			for f in digraph.adj_e(e.dst):
				if not self.visited(f.dst):
					pqueue.push(self.distances[f.src] + f.weigth, f)
