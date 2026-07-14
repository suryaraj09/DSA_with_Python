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
12. sort
13. min
14. max
15. sum
16. extend
17. negative indexing
18. Slicing
19. Merge
20. count
    """

import ctypes

class MyList:
    

    def __init__(self):
        self.size = 1
        self.n = 0
        # Create a C type array with size = self.size

        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        # Creates a C type array with given capacity
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.n

    def __append__(self,value):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.A[self.n] = value
        self.n += 1
    def __getitem__(self,index):
        if index < 0 or index >= self.n:
            raise IndexError('Index out of range')
        return self.A[index]

    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + " , "

        return '[' + result[: -2] + ']'

    def __getitem__(self,index):
        if 0<= index <= self.n:
            return self.A[index]
        else:
            return 'IndexError:- Index out of range'
    
    def __pop__(self):
        if self.n == 0:
            return 'IndexError:- Index out of range'
        value = self.A[self.n-1]
        self.A[self.n-1] = None
        self.n -= 1

    def __clear__(self):
        self.n = 0
        self.size = 1
        return self.A

    def __find__(self, itemvalue):
        for i in range(self.n):
            if self.A[i] == itemvalue:
                return i
        return "Element not found"
    
    def __insert__(self,pos, item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    def __remove__(self, item):
        pos = self.__find__(item)

        if type(pos) == int:
            #delete
            self.__delitem__(pos)
        else:
            return pos


    def __delitem__(self, pos):
        #check if index is valid
        for i in range (pos, self.n-1):
            self.A[i] = self.A[i+1]
        self.n -= 1
        if self.n > 0 and self.n == self.size//4:
            self.__resize(self.size//2)




# testing purpose
m = MyList()
m.__append__(10)
m.__append__(20)
m.__append__(30)
m.__append__(40)
m.__append__(50)
m.__append__("hello")
print(m.__find__(50))
m.__remove__("hello")
print(m)
print(len(m))





