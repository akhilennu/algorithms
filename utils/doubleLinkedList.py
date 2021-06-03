class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.setNext(next)
        self.setPrev(prev)
        self.data = data

    def setNext(self, next):
        self.next = next
        if(next != None):
            next.prev = self

    def setPrev(self, prev):
        self.prev = prev
        if(prev != None):
            prev.next = self

    # Always use head.displayNodes

    def displayNodes(self):
        originalNode = self
        node = self
        print(end='-')
        print('|', node.data, '|', end='-')
        while(node.next != None and node.next != originalNode):
            node = node.next
            print('|', node.data, '|', end='-')
        print()


a = Node(data=5)
b = Node(data=7, next=a)
c = Node(data=8, next=b)

a.setNext(c)

a.displayNodes()
b.displayNodes()
c.displayNodes()

print()
print(c.prev.data)
