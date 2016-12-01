from heapq import *
class NQueue(object):
    """docstring for NQueue."""
    def __init__(self, key, value):
        super(NQueue, self).__init__()
        self.key = key
        self.value = value

    def __cmp__(self, other):
        return cmp(self.key, other.key)

class PQueue(object):
    """docstring for PQueue."""
    def __init__(self):
        super(PQueue, self).__init__()
        self.heap = []
        self.dict = {}

    def push(self, key, value):
        nqueue = NQueue(key, value)
        heappush(self.heap, nqueue)
        self.dict[value] = nqueue

    def pop(self):
        value = heappop(self.heap).value
        del self.dict[value]
        return value

    def top(self):
        return self.heap[0].value

    def empty(self):
        return len(self.heap) == 0

    def __contains__(self, value):
        return value in self.dict

    def __setitem__(self, value, key):
        self.dict[value].key = key
        heapify(self.heap)

    def __getitem__(self, value):
        return self.dict[value].key
