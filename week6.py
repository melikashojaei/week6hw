#سوال3
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def get_element_at(self, index):
        if index < len(self.items):
            return self.items[index]
        else:
            return "Index out of range"

#سوال5
class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else "Queue is empty"


#سوال6
class QueueWithArray:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            return "Queue is full"
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return "Queue is empty"
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item


