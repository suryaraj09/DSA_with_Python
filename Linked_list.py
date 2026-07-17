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

    def __insertMiddle__(self, after, value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after: 
                break
            curr = curr.next

        # case 1 break -> Item mil gaya -> curr -> not none
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
            return
        # case 2 break -> item nahi mila -> curr -> None
        else:
            print("Item not found")
        return

    def __traversal__(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

    def __clear__(self):
        self.head = None
        self.n = 0
        return True

    def __headDelete__(self):
        if self.head == None:
            print("empty list")
            return False
        self.head = self.head.next
        self.n -= 1
        return True

    def __POP__(self):
        if self.head == None:
            print("empty linked list")
            return None

        curr = self.head
        # have to check for the one item in the LL
        if curr.next == None:
            val = curr.data
            self.__headDelete__()
            return val
        while curr.next.next != None:
            curr = curr.next
        popped_val = curr.next.data
        curr.next = None
        self.n -= 1
        return popped_val

# searching the index by the value
    def __find__(self, item):
        curr  = self.head
        pos = 0

        while curr != None:
            if curr.data  == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return "position not found"

#seaching the value from the index

    def getitem(self, index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1
        return "the postional value not found"

        return curr.data


    def __remove__(self, value):
        # Case 1: Empty list check
        if self.head == None:
            print("Empty list")
            return

        # Case 2: Item to remove is at the head
        if self.head.data == value:
            self.head = self.head.next
            self.n -= 1
            return

        # Case 3: Item to remove is in the middle or tail
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                curr.next = curr.next.next
                self.n -= 1
                return
            curr = curr.next

        # Case 4: Item not found
        print("Item Not Found")

l = Linked_list()
l.__insertHead__(1)
l.__insertHead__(2)
l.__insertHead__(3)
l.__insertHead__(4)

# l.__insertTail__(6)
# l.__insertTail__(11)
# l.__insertMiddle__(11, 20)
# l.__insertMiddle__(2, 8)
# l.__POP__()
# l.__POP__()
# l.__POP__()
# l.__POP__()
# l.__POP__()
# l.__remove__(2)
# l.__remove__(4)
# l.__remove__(3)
# l.__remove__(1)

# print("The search of the index resulted\n")
# print(l.__find__(10))
print("\nThe traversal of the Linked list\n")
print(l.getitem(3))
l.__traversal__()
