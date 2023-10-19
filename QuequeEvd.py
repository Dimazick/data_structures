class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class QuequeEvd:
    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None

    def enqueue(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeaue(self):
        if self.head is None:
            print("Queque пуста")
            pass
        res = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return res

    def peek(self):
        print("head = ", self.head.data)

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


polikl = QuequeEvd()
polikl.enqueue(5)
polikl.enqueue(7)
print('count = ', polikl.size)
polikl.enqueue(123)
print(5, 7, 123)
print("deque = ", polikl.dequeaue())
print('count after deque = ', polikl.size)

polikl.peek()
polikl.dequeaue()
print("мы еще раз декюикюи")
polikl.peek()

