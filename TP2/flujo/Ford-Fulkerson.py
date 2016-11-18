#!/usr/bin/env python

from digraph import*
from edge import*
from math import log
from bfs import*

class Edge_f(Edge):
	def __init__(self,src,dst,weigth,flow):
		super(Edge_f,self).__init__(src,dst,weigth)
		self.flow=flow


#el nodo 0 es tomado como la fuente de flujo y el nodo 1 como el sumidero de flujo
class Ford_Fulkerson(object):
	def residual_digraph(self,digraph,scaling,flow):
		residual_edges={}
		residual=Digraph(digraph.v())
		for key,edge in self.flow.items():
			if edge.flow>=scaling:
				residual.add_edge(edge.dst,edge.src,edge.flow)
				residual_edges[(edge.dst,edge.src)]=self.backward
			if edge.weigth-edge.flow>=scaling:
				residual.add_edge(edge.src,edge.dst,edge.weigth-edge.flow)
				residual_edges[(edge.src,edge.dst)]=self.forward
		return (residual, residual_edges)

	def augment(self,bfs,residual_edges):
		v=self.t
		path=[]
		while v!=self.s:
			path.append(bfs.edge_to(v))
			v=bfs.edge_to(v).src
		bottleneck=float('inf')
		for e in path:
			if e.weigth<bottleneck:
				bottleneck=e.weigth
		for e in path:
			if residual_edges[(e.src,e.dst)]==self.forward:
				self.flow[(e.src,e.dst)].flow+=bottleneck
			else
				self.flow[(e.dst,e.src)].flow-=bottleneck
				

	def __init__(self, digraph):
		self.s=0
		self.t=1
		self.forward=0
		self.backward=1
		self.flow={}
		min_c=float('inf')
		for e in digraph.adj_e(s):
			if e.weigth<min_c:
				min_c=e.weigth
		scaling=2**int(log(min_c,2))
		for e in digraph.iter_edges():
			self.flow[(e.src,e.dst)]=Edge_f(e.src,e.dst,e.weigth,0)

		while scaling>=1:
			residual,residual_edges=self.residual_digraph(digraph,scaling)
			bfs=BFS(residual,s,t)
			while bfs.dst_visited():
				self.augment(bfs,flow,residual_edges)
				residual,residual_edges=self.residual_digraph(digraph,scaling,flow)
				bfs=BFS(residual,s,t)
			scaling/=2
		self.min_cut=[]
		for v in digraph.__iter__():
			if bfs.visited(v):self.min_cut.append(v)

	def get_min_cut(self):
		return self.min_cut

	def get_flow(self):
		return self.flow
		
