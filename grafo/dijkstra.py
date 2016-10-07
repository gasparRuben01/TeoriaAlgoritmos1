#!/usr/bin/env python

import paths
import heapq


class Dijkstra(paths.Paths):
	def __init__(self, digraph, origin, destiny, heuristica=lambda v: 0):
		paths.Paths.__init__(self, digraph, origin, destiny)
		self.heuristica=heuristica		
		v=origin
		self.distance(origin)=0
		#arista falsa para empezar con el algoritmo
		#les agrego un campo que tiene el peso del paht completo mas la heuristica
		heap=[0, (0, origin, origin)]
		while heap:
			e=heapq.heappop(heap)
			self.distance[e[1][2]]=self.distance[e[1][1]]+e[1][0]
			self.edges[e[1][2]]=e[1]
			#corto si encuentro destino
			if e[1][2]==destiny: break
			for i in digraph.adj_e(e[1][2]):
				#la arista i es la normal del grafo o sea la 3 campos (weigth, origin, destiny)
				if self.distance(i[2])==float('inf'):
					heapq.heappush((i[0]+self.distace[i[1]]-h(i[1])+h(i[2]), i))
		#la arista de la raiz quedo fijada con el valor falso (0, origin, origin), por la que la set en null
		self.edges[origin]=None
		
