# odd positional item has to be summed hehehehe

from Linked_list import Linked_list
def sum_odd_nodes(self):
    temp = self.head
    counter = 0
    result = 0

    while temp != None:
        if counter %2 != 0:
            result = result + temp.data
        counter +=1 
        temp = temp.next
    return result

# dynamically add sum_odd_nodes to Linked_list class
Linked_list.sum_odd_nodes = sum_odd_nodes

# test execution block
if __name__ == "__main__":
    # Create the linked list and populate it
    ll = Linked_list()
    ll.__insertHead__(10)
    ll.__insertHead__(25)
    ll.__insertHead__(5)
    ll.__insertHead__(15)

    print("Original Linked List traversal:")
    ll.__traversal__()

    print("\nSum of odd positional nodes:", ll.sum_odd_nodes())