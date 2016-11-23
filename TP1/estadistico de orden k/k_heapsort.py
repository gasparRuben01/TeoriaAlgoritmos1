#!/usr/bin/python
from heap import *

def k_heapsort(elements, k):
    heap = Heap()
    heap.pushAll(elements)
    e = 0
    for _ in range(k+1):
        e = heap.pop()

    return e
