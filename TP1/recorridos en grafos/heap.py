#!/usr/bin/python
from heapq import *

class Heap(object):
    """docstring for Heap."""
    def __init__(self):
        super(Heap, self).__init__()
        self.heap = []

    def push(self, arg):
        heappush(self.heap, arg)

    def pop(self):
        return heappop(self.heap)

    def pushAll(self, elements):
        self.heap = elements
        heapify(self.heap)

    def top(self):
        return self.heap[0]

    def empty(self):
        return len(self.heap) == 0
