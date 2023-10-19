class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class QuequeEvd:
    def __init__(self):
        self.count = 0
        self.last = None
        self.first = None

    def enqueue_to_last(self, data):
        node = Node(data)
        if self.count == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.count += 1

    def enqueue_to_first(self, data):
        node = Node(data)
        if self.count == 0:
            self.first = node
            self.last = node
        else:
            self.first.next = node
            self.first = node
        self.count += 1

    def dequeaue(self):
        if self.first is None:
            print("Queque пуста")
            pass
        res = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.count -= 1
        return res

    def show(self):
        print("first = ", self.first.data)
        print("last = ", self.last.data)

polikl = QuequeEvd()
polikl.enqueue(5)
polikl.enqueue(7)
print('count = ', polikl.count)
polikl.enqueue(123)
print(5, 7, 123)
print("deque = ", polikl.dequeaue())
print('count after deque = ', polikl.count)

polikl.show()
polikl.dequeaue()
print("мы еще раз декюикюи")
polikl.show()