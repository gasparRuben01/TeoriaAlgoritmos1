#!/usr/bin/env python
from paths import *
from digraph import *
from pqueue import *
from edge import *

class AStar(Paths):
    """docstring for AStar."""
    def __init__(self, digraph, origin, destiny, heuristic = lambda v: 0):
        super(AStar, self).__init__(digraph, origin, destiny)
        pqueue = PQueue()

        for e in digraph.adj_e(origin):
            h = e.weigth + heuristic(e.dst) - heuristic(e.src)
            pqueue.push(h, e)

    	while not pqueue.empty():
    		e = pqueue.pop()
    		if self.visited(e.dst): continue

    		self.distances[e.dst] = self.distances[e.src] + e.weigth
    		self.edges[e.dst] = e.src
    		if self.dst_visited(): break

    		for f in digraph.adj_e(e.dst):
    			if not self.visited(f.dst):
					h = f.weigth + heuristic(f.dst) - heuristic(f.src)
					pqueue.push(h, f)
