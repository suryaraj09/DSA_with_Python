"""Dynamic Array implementation using Python.
1. Create List
2. Len
3. append
4. print
5. indexing
6. pop
7. clear
8. find
9. insert
10. delete
11. remove
    """

import ctypes

class MyList:
    

    def __init__(self):
        self.size = 1
        self.n = 0
        # Create a C type array with size = self.size

        self.A = self.__make_array(self.size)

    def __make_array(slef,capacity):
        # Creates a C type array with given capacity
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.n

    def __append__(self,value):
        self.A[self.n] = value
        self.n += 1  
     