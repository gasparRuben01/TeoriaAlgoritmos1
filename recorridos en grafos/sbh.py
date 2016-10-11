#!/usr/bin/env python
from paths import *
from digraph import *
from pqueue import *
from edge import *

#search by heuristic
class SBH(Paths):
    """docstring for SBH."""
    def __init__(self, digraph, origin, destiny, heuristic = lambda v: 0):
        super(SBH, self).__init__(digraph, origin, destiny)
        pqueue = PQueue()
        pqueue.push(heuristic(origin), origin)
        while not pqueue.empty() and not self.dst_visited():
            u = pqueue.pop()
            for e in digraph.adj_e(u):
                if not self.visited(e.dst):
                    self.distances[e.dst] = self.distances[e.src] + e.weigth
                    self.edges[e.dst] = e.src
                    if self.dst_visited(): break

                    pqueue.push(heuristic(e.dst), e.dst)
