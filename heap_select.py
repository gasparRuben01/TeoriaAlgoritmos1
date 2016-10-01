#!/usr/bin/env python

import heapq
import functools

@functools.total_ordering
class ReverseCompare(object):
	def __init__(self, obj):
		self.obj=obj
	def __eq__(self, other):
		return self.obj==other.obj
	def __lt__(self, other):
		return self.obj>other.obj

def heap_select(elements, k):	
	""" Si k>0: retorna el k-esimo elemento mas pequenio, en caso de que k>len(elements), retorna el maximo
	    Si k ==0: retorna el minimo
	    Si k<0: retorna el k-esimo elemento mas grande, en caso de que |k|>len(elements), retorna el minimo"""
	if k>0:
		heap=map(ReverseCompare, elements[:k])
		comparar= lambda e1, e2: e1<e2.obj
		push= lambda heap, e: heapq.heappush(heap, ReverseCompare(e))
		pop= lambda heap: heapq.heappop(heap).obj
	elif k==0:
		#no tiene sentido hacer un heap de size 0, asi que busco el minimo y listo
		return min(elements)
	else:	
		k=-k
		heap=elements[:k]
		comparar= lambda e1, e2: e1>e2
		push= lambda heap, e: heapq.heappush(heap, e)
		pop= lambda heap: heapq.heappop(heap)

	heapq.heapify(heap)
	for i in elements[k:]:
		if comparar(i, heap[0]):
			pop(heap)
			push(heap, i)
	
	return pop(heap)

