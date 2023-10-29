class Node:
    def __init__(self, data = 0):
        self.data = data
        self.nextItem = None
    
    def __repr__(self):
        return '%s => %s' % (self.data, self.nextItem)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return '%s' % (self.head)

    def append(self, data):
        node = Node(data)

        node.nextItem = self.head
        self.head = node

    def print_list(self):
        print(self.__repr__())

def count_nodes(linked_list):
    navegar = linked_list.head
    count = 0
    while navegar != None:
        count += 1
        navegar = navegar.nextItem
    print("Número de nós: ", count)


linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.append(5)
linkedList.append(6)
linkedList.append(7)
linkedList.print_list()

count_nodes(linkedList)