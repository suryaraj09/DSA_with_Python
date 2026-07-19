# Write a python program to find the maximum value in the linked list and replace it with a given value. Assume that the linked list is populated with the whole numbers and there is only one maximum value in the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self,data):
        self.data = data
    def set_next(self,next):
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
    def display(self):
        current = self.head
        while current != None:
            print(current.data,end=" ")
            current = current.next
    def find_max(self):
        current = self.head
        max_val = current.data
        while current != None:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val
    def replace_max(self,val):
        current = self.head
        while current != None:
            if current.data == self.find_max():
                current.data = val
            current = current.next

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
print("Original list")
ll.display()
print("\nList after replacing max value with 0")
ll.replace_max(0)
ll.display()
