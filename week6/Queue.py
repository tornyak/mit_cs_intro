__author__ = 'vanja'

class Queue(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        self.vals.append(e)

    def remove(self):
        if not len(self.vals) > 0:
            raise ValueError()
        else:
            return self.vals.pop(0)

queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove()

queue.insert(7)
print queue.remove()

print queue.remove()

#queue.remove()