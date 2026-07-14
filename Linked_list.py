"""Insert, Traverse, Delete, search operations on Linked List
Insert - occurs from head, tail or middle 
Traverse - occurs from head to tail only
Delete :- Head, Tail (pop) Value(remove) Index(pop at index) 
search:- value, index"""

class Node:

    def __init__(self, value):
        
        self.data = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

print(a.data)
print(a.next)

print(b.data)
print(b.next)

print(c.data)
print(c.next)

class Linked_list:

    def __init__(self):
        self.head = None
        self.n = 0
        

    def __len__(self):
        return self.n

    def __insertHead__(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

    def __insertTail__(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1
        return

    def __traversal__(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

l = Linked_list()
l.__insertHead__(1)
l.__insertHead__(2)
l.__insertHead__(3)
l.__insertHead__(4)

l.__insertTail__(6)
l.__traversal__()
