# Complete Python Lists Guide

## What Are Lists?

List is a built-in dynamic array which can store elements of different data types. It is an ordered collection of item, that is elements are stored in the same order as they were inserted into the list. List stores references to the objects (elements) rather than storing the actual data itself..

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2]]
empty = []
```

## Creating Lists

```python
# Direct creation
fruits = ["apple", "banana", "cherry"]

# Using list() constructor
numbers = list(range(5))  # [0, 1, 2, 3, 4]
chars = list("hello")     # ['h', 'e', 'l', 'l', 'o']

# List multiplication
zeros = [0] * 5           # [0, 0, 0, 0, 0]
```

## Accessing Elements

```python
fruits = ["apple", "banana", "cherry", "date"]

# Positive indexing (starts at 0)
first = fruits[0]         # "apple"
second = fruits[1]        # "banana"

# Negative indexing (starts at -1 from end)
last = fruits[-1]         # "date"
second_last = fruits[-2]  # "cherry"

# Slicing [start:end:step]
subset = fruits[1:3]      # ["banana", "cherry"]
all_fruits = fruits[:]    # Full copy
reversed_fruits = fruits[::-1]  # Reverse order
every_other = fruits[::2] # ["apple", "cherry"]
```

## Modifying Lists

```python
fruits = ["apple", "banana", "cherry"]

# Change single element
fruits[0] = "apricot"     # ["apricot", "banana", "cherry"]

# Change multiple elements
fruits[1:3] = ["blueberry", "coconut"]  # ["apricot", "blueberry", "coconut"]

# Delete elements
del fruits[0]             # ["blueberry", "coconut"]
del fruits[1:3]           # Delete slice
```

## Essential List Methods

### Adding Elements
```python
fruits = ["apple"]

# append() - adds single element to end
fruits.append("banana")         # ["apple", "banana"]

# insert() - adds element at specific position
fruits.insert(1, "cherry")      # ["apple", "cherry", "banana"]

# extend() - adds multiple elements
fruits.extend(["date", "fig"])  # ["apple", "cherry", "banana", "date", "fig"]
```

### Removing Elements
```python
fruits = ["apple", "banana", "cherry", "banana"]

# remove() - removes first occurrence
fruits.remove("banana")    # ["apple", "cherry", "banana"]

# pop() - removes and returns element
last = fruits.pop()        # Returns "banana", list becomes ["apple", "cherry"]
first = fruits.pop(0)      # Returns "apple", list becomes ["cherry"]

# clear() - removes all elements
fruits.clear()             # []
```

### Finding Elements
```python
numbers = [1, 2, 3, 2, 4]

# index() - returns index of first occurrence
pos = numbers.index(2)     # 1

# count() - counts occurrences
count = numbers.count(2)   # 2

# Check if element exists
exists = 3 in numbers      # True
not_exists = 5 not in numbers  # True
```

### Sorting and Reversing
```python
numbers = [3, 1, 4, 1, 5]

# sort() - sorts in place
numbers.sort()             # [1, 1, 3, 4, 5]
numbers.sort(reverse=True) # [5, 4, 3, 1, 1]

# sorted() - returns new sorted list
original = [3, 1, 4]
new_sorted = sorted(original)  # original unchanged

# reverse() - reverses in place
numbers.reverse()          # Reverses current order
```

## List Operations

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2   # [1, 2, 3, 4, 5, 6]

# Repetition
repeated = list1 * 3       # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Length
length = len(list1)        # 3

# Min/Max (for comparable elements)
numbers = [3, 1, 4, 1, 5]
minimum = min(numbers)     # 1
maximum = max(numbers)     # 5
total = sum(numbers)       # 14
```

## List Comprehensions

Concise way to create lists based on existing iterables:

```python
# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Transform strings
words = ["hello", "world"]
upper_words = [word.upper() for word in words]  # ["HELLO", "WORLD"]

# Nested comprehensions
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

## Copying Lists

```python
original = [1, 2, [3, 4]]

# Shallow copy (copies list but not nested objects)
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# Deep copy (copies everything including nested objects)
import copy
deep_copy = copy.deepcopy(original)
```

## Iterating Over Lists

```python
fruits = ["apple", "banana", "cherry"]

# Basic iteration
for fruit in fruits:
    print(fruit)

# With index using enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Iterate over multiple lists with zip()
colors = ["red", "yellow", "red"]
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")
```

## Nested Lists

```python
# 2D list (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access elements
element = matrix[1][2]  # 6 (row 1, column 2)

# Modify elements
matrix[0][0] = 10       # [[10, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4, 5, 6]
```

## Performance Tips

```python
# Use list comprehensions instead of loops when possible
# Good
squares = [x**2 for x in range(1000)]

# Slower
squares = []
for x in range(1000):
    squares.append(x**2)

# Use extend() instead of multiple append() calls
# Good
my_list.extend([1, 2, 3])

# Slower
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Preallocate size if known
my_list = [None] * 1000  # Then assign values
```

## Common Patterns

```python
# Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Chunk list into smaller lists
def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

# Find all indices of an element
def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

# Rotate list
def rotate_list(lst, n):
    return lst[n:] + lst[:n]
```

## Memory Considerations

- Lists are dynamic arrays that may over-allocate for efficiency
- Use `array.array()` for large numeric lists to save memory
- Use `collections.deque` for frequent insertions/deletions at both ends
- Consider generators for large datasets that don't need to be stored entirely in memory

## Common Gotchas

```python
# Mutable default arguments
def bad_function(lst=[]):  # DON'T DO THIS
    lst.append(1)
    return lst

def good_function(lst=None):  # DO THIS
    if lst is None:
        lst = []
    lst.append(1)
    return lst

# Shallow copy issues
original = [[1, 2], [3, 4]]
copy = original.copy()
copy[0][0] = 99  # This changes original[0][0] too!

# List multiplication with mutable objects
matrix = [[0] * 3] * 3  # DON'T DO THIS - all rows are the same object
matrix = [[0] * 3 for _ in range(3)]  # DO THIS
```

That's everything you need to know about Python lists. They're versatile, efficient, and essential for Python programming.