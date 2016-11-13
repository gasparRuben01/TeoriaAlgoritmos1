from heap import *
class NQueue(object):
    """docstring for NQueue."""
    def __init__(self, key, value):
        super(NQueue, self).__init__()
        self.key = key
        self.value = value

    def __cmp__(self, other):
        return self.key - other.key

class PQueue(object):
    """docstring for PQueue."""
    def __init__(self):
        super(PQueue, self).__init__()
        self.heap = Heap()

    def push(self, key, value):
        self.heap.push(NQueue(key, value))

    def pop(self):
        return self.heap.pop().value

    def top(self):
        return self.heap.top().value

    def empty(self):
        return self.heap.empty()
