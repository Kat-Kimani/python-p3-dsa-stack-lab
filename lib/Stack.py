class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = list(items)
        self.limit = limit

    def is_empty(self):
        return len(self.items) == 0

    def full(self):
        return len(self.items) >= self.limit

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise IndexError("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1
