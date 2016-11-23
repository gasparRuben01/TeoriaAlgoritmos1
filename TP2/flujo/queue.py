class Queue(object):
    """docstring for Queue."""
    def __init__(self):
        super(Queue, self).__init__()
        self.queue = []

    def push(self, arg):
        self.queue.append(arg)

    def pop(self):
        return self.queue.pop(0)

    def empty(self):
        return len(self.queue) == 0
