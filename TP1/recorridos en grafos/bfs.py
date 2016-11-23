from paths import *
from digraph import *
from queue import *
from edge import *

class BFS(Paths):
	"""docstring for BFS."""
	def __init__(self, digraph, origin, destiny, heuristic = lambda v: 0):
		super(BFS, self).__init__(digraph, origin, destiny)
		queue = Queue()
		queue.push(origin)
		while not queue.empty() and not self.dst_visited():
			u = queue.pop()
			for e in digraph.adj_e(u):
				if not self.visited(e.dst):
					self.distances[e.dst] = self.distances[u] + e.weigth
					self.edges[e.dst] = e.src
					if self.dst_visited(): break

					queue.push(e.dst)
