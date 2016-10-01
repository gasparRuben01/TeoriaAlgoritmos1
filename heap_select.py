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
	heap=map(ReverseCompare, elements[:k])
	heapq.heapify(heap)
	for i in elements[k:]:
		i=ReverseCompare(i)
		if (i>heap[0]):
			heapq.heappop(heap)
			heapq.heappush(heap, i)
	return heap[0].obj
