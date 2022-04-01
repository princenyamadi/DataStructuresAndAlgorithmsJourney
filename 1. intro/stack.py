# * different ways for implementing stack
# ? you can pop from the top of the stack
# ? you can push to the top of the stack

# stack implementation using list
data = []

data.append(1)
data.append(2)
data.append(3)
data.append(4)

element = data.pop()
print(element)

print(data)
peek = data[len(data) - 1]

print(peek)

# stacks are last in first out
#
