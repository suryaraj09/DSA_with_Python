# Write a python program to reverse a linked list containing integer data
from Linked_list import Linked_list

def reverse(self):
    curr = self.head
    prev = None
    next = curr.next
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    self.head = prev

Linked_list.reverse = reverse

if __name__ == "__main__":
    # Create the linked list and populate it
    ll = Linked_list()
    ll.__insertHead__(10)
    ll.__insertHead__(25)
    ll.__insertHead__(5)
    ll.__insertHead__(15)

    print("Original Linked List traversal:")
    ll.__traversal__()

    ll.reverse()
    print("Reversed Linked List traversal:")
    ll.__traversal__()
