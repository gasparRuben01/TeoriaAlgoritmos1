import paths

class BFS(paths.Paths):
	def __init__(self, digraph, origin, destiny):
		if digraph.v()<origin:
			raise ValueError("no existe vertice origin")

		paths.Paths.__init__(self, digraph, origin)
		cola=[origin]
		self.distances[origin]=0
		v=origin
		while cola and v!=destiny:
			v=cola.pop(0)
			for i in digraph.adj_e(v):
				if self.distances[i[2]]==float('inf'):
					self.distances[i[2]]=self.distances[v]+1
					self.edges[i[2]]=i
					#corto ejecucion cuando encuentro destino
					if i[2]==destiny: break
					cola.append(i[2])

