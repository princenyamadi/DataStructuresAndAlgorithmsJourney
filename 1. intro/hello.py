# *
# * STACK

from collections import deque
data = []
data.append(5)
# element = data.pop()

# print(element)
print(data[len(data) - 1])
data.append(10)
data.append(15)
data.append(20)
data.append(25)

data.pop()
data.pop()
print(data)


# * QUEUE

data = []
data.append(5)
# element = data.pop()

# print(element)
print(data[len(data) - 1])
data.append(10)
data.append(15)
data.append(20)
data.append(25)

data.pop(0)

print(data)


data = deque()
data.append("Caleb")
element = data.popleft()
print(element, data)


# CUSTOM IMPLEMENTATION USING STACK

class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()


stack = Stack()

stack.push(10)
test = stack.pop()
