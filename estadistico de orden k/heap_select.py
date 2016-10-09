#!/usr/bin/python
from heap import *

def heap_select(elements, k):
	heap = Heap()
	for i in elements[:k+1]:
		heap.push(-i)

	for i in elements[k+1:]:
		if i < -heap.top():
			heap.pop()
			heap.push(-i)
	
	return -heap.top()
