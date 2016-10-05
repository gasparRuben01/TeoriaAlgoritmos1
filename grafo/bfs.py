import paths

class BFS(paths.Paths):
	def __init__(self, digraph, origin):
		if digraph.v()<origin:
			raise ValueError("no existe vertice origin")

		paths.Paths.__init__(self, digraph, origin)
		cola=[origin]
		self.distances[origin]=0
		while cola:
			v=cola.pop(0)
			for i in digraph.adj_e(v):
				if self.distances[i[1]]==float('inf'):
					self.distances[i[1]]=self.distances[v]+1
					self.edges[i[1]]=i
					cola.append(i[1])

