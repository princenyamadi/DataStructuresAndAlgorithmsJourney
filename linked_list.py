class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


list = LinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")


# Link first Node to second node
list.head.next = e2

# Link second Node to third node
e2.next = e3
print(type(list.head))

list.print_list()
