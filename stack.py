class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.count = 0
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        pushing = self.top.data
        self.top = self.top.next
        self.count -= 1
        return pushing

    def peek(self):
        print(self.top.data)

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False



sta4ka = Stack()
sta4ka.push(4)
sta4ka.push(8)
sta4ka.push(12)
print(4, 8, 12)
sta4ka.peek()
print("count =  ", sta4ka.count)
print("pop ", sta4ka.pop())
print("pop ", sta4ka.pop())
print("count =  ", sta4ka.count)
print(sta4ka.top.data)
print('1 test is empty ', sta4ka.is_empty())
sta4ka.pop()
print('2nd test is empty', sta4ka.is_empty())