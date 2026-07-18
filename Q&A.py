
from Linked_list import Node
def fun(head):
    
    if head.next != None and head.next.next != None:
        return head.data
    if head.next.next != None:
        fun(head.next)
    print(head.data, "", end ='')
    fun(head.next)
    print(head.data, "", end='')


# 2. Create the linked list nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5) 

# 3. Link them together
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# 4. Call the function passing the head node (n1)
fun(n1)
