# DSA with Python

A learning repository containing implementations of core data structures and algorithms in Python. This project demonstrates how fundamental data structures work at a lower level, with a focus on understanding the underlying mechanics rather than relying on built-in libraries.

## Contents

### Data Structures Implemented

#### Dynamic Array (`Dynamic_Array.py`)
A custom implementation of a dynamic array (resizable list) from scratch using Python's `ctypes` module to interact with C-level memory.

**Features:**
- Automatic resizing when capacity is exceeded
- Common list operations: append, insert, delete, remove, pop
- Indexing and slicing support
- Search, sort, min, max, and sum operations
- Negative indexing support
- Array merging and element counting

**Key Methods:**
- `__append__(value)` - Add element to the end
- `__insert__(pos, item)` - Insert element at specific position
- `__remove__(item)` - Remove element by value
- `__pop__()` - Remove and return last element
- `__find__(itemvalue)` - Search for element
- `__delitem__(pos)` - Delete at specific index

#### Linked List (`Linked_list.py`)
A node-based linked list implementation with support for various insertion, deletion, and search operations.

**Features:**
- Insert at head, tail, or middle of the list
- Traverse the entire list
- Delete from head or tail (pop)
- Remove element by value
- Search by value or index
- Track list length

**Key Methods:**
- `__insertHead__(value)` - Insert at beginning
- `__insertTail__(value)` - Insert at end
- `__insertMiddle__(after, value)` - Insert after a specific value
- `__headDelete__()` - Remove first element
- `__POP__()` - Remove and return last element
- `__remove__(value)` - Remove by value
- `__find__(item)` - Search by value
- `getitem(index)` - Get value at index
- `__traversal__()` - Print all elements

## Getting Started

### Prerequisites
- Python 3.x

### Running the Code

Each file can be executed directly to run its built-in test cases:

```bash
python Dynamic_Array.py
python Linked_list.py
```

### Example Usage

**Dynamic Array:**
```python
m = MyList()
m.__append__(10)
m.__append__(20)
m.__append__(30)
print(m)  # [10 , 20 , 30]
print(len(m))  # 3
m.__remove__(20)
print(m)  # [10 , 30]
```

**Linked List:**
```python
l = Linked_list()
l.__insertHead__(1)
l.__insertHead__(2)
l.__insertHead__(3)
l.__traversal__()  # Prints: 3, 2, 1
print(l.__find__(2))  # 1 (index)
```

## Learning Objectives

This repository helps understand:
- How dynamic arrays resize and manage memory
- Pointer-based data structures (linked lists)
- Time and space complexity of common operations
- Low-level memory management in Python using `ctypes`
- Fundamental algorithm operations (insert, delete, search, traverse)

## Future Additions

Potential data structures to implement:
- Stacks
- Queues
- Trees (Binary Search Trees, AVL Trees)
- Graphs
- Hash Tables
- Heaps

## Notes

- These implementations prioritize educational clarity over production performance
- The dynamic array uses `ctypes` to demonstrate low-level memory concepts
- Both data structures include basic error handling and edge case management
- Test cases are included at the bottom of each file for reference

## Contributing

Feel free to explore, modify, and experiment with these implementations to deepen your understanding of data structures!

## License

This project is open source and available for educational purposes.
