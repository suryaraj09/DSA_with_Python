# Write a python program to find the maximum value in the linked list and replace it with a given value. Assume that the linked list is populated with the whole numbers and there is only one maximum value in the linked list

from Linked_list import Linked_list

def replace_max(self, value):
    if self.head == None:
        return

    max_node = self.head
    temp = self.head.next
    
    while temp != None:
        if temp.data > max_node.data:
            max_node = temp
        temp = temp.next


    max_node.data = value

Linked_list.replace_max = replace_max

# Test execution block
if __name__ == "__main__":
    # Create the linked list and populate it
    ll = Linked_list()
    ll.__insertHead__(10)
    ll.__insertHead__(25)  # This will be the maximum
    ll.__insertHead__(5)
    ll.__insertHead__(15)
    
    print("Original Linked List traversal:")
    ll.__traversal__()
    
    print("\nReplacing maximum value with 99...")
    ll.replace_max(99)
    
    print("\nUpdated Linked List traversal:")
    ll.__traversal__()
