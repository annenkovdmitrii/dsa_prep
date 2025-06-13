# Complete Python Tuples Guide

## What Are Tuples?

Tuples are ordered, immutable collections that can store any data type. They're defined with parentheses `()` or just commas. Once created, you cannot change their contents.

```python
coordinates = (10, 20)
mixed = (1, "hello", 3.14, True, [1, 2])
empty = ()
single = (42,)  # Note the comma for single-element tuples
```

## Creating Tuples

```python
# Direct creation with parentheses
point = (3, 4)
colors = ("red", "green", "blue")

# Parentheses optional (except for empty tuple)
point = 3, 4
colors = "red", "green", "blue"

# Using tuple() constructor
from_list = tuple([1, 2, 3])        # (1, 2, 3)
from_string = tuple("hello")        # ('h', 'e', 'l', 'l', 'o')
from_range = tuple(range(5))        # (0, 1, 2, 3, 4)

# Single element tuple (comma is crucial)
single = (42,)    # Tuple with one element
not_tuple = (42)  # This is just an integer in parentheses

# Empty tuple
empty = ()
empty2 = tuple()
```

## Accessing Elements

```python
fruits = ("apple", "banana", "cherry", "date")

# Positive indexing (starts at 0)
first = fruits[0]         # "apple"
second = fruits[1]        # "banana"

# Negative indexing (starts at -1 from end)
last = fruits[-1]         # "date"
second_last = fruits[-2]  # "cherry"

# Slicing [start:end:step]
subset = fruits[1:3]      # ("banana", "cherry")
all_fruits = fruits[:]    # Full copy
reversed_fruits = fruits[::-1]  # Reverse order
every_other = fruits[::2] # ("apple", "cherry")
```

## Tuple Operations

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2   # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 3        # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Length
length = len(tuple1)         # 3

# Membership testing
exists = 2 in tuple1         # True
not_exists = 7 not in tuple1 # True

# Min/Max (for comparable elements)
numbers = (3, 1, 4, 1, 5)
minimum = min(numbers)       # 1
maximum = max(numbers)       # 5
total = sum(numbers)         # 14
```

## Tuple Methods

Tuples have only two methods since they're immutable:

```python
numbers = (1, 2, 3, 2, 4, 2)

# count() - counts occurrences of a value
count_twos = numbers.count(2)  # 3

# index() - returns index of first occurrence
first_two = numbers.index(2)   # 1

# index() with start and end parameters
next_two = numbers.index(2, 2)  # 3 (start searching from index 2)
```

## Tuple Packing and Unpacking

One of the most powerful features of tuples:

```python
# Packing - creating tuple from separate values
point = 3, 4              # Same as point = (3, 4)
person = "John", 30, "NYC"

# Unpacking - extracting values from tuple
x, y = point              # x = 3, y = 4
name, age, city = person  # name = "John", age = 30, city = "NYC"

# Swapping variables (uses tuple packing/unpacking)
a, b = 10, 20
a, b = b, a              # Now a = 20, b = 10

# Partial unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers  # first = 1, middle = [2, 3, 4], last = 5
first, *rest = numbers          # first = 1, rest = [2, 3, 4, 5]
*all_except_last, last = numbers # all_except_last = [1, 2, 3, 4], last = 5

# Ignore values with underscore
_, y = point             # Only care about y coordinate
name, _, city = person   # Ignore age
```

## Iterating Over Tuples

```python
colors = ("red", "green", "blue")

# Basic iteration
for color in colors:
    print(color)

# With index using enumerate()
for i, color in enumerate(colors):
    print(f"{i}: {color}")

# Iterate over multiple tuples with zip()
sizes = ("small", "medium", "large")
for color, size in zip(colors, sizes):
    print(f"{color} {size}")

# Unpacking in loops
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"Point: ({x}, {y})")
```

## Nested Tuples

```python
# 2D points
triangle = ((0, 0), (3, 0), (1.5, 2.6))

# Access nested elements
first_point = triangle[0]     # (0, 0)
first_x = triangle[0][0]      # 0
first_y = triangle[0][1]      # 0

# Unpack nested tuples
(x1, y1), (x2, y2), (x3, y3) = triangle

# Mixed nesting
data = ("header", (1, 2, 3), ["a", "b", "c"])
header, numbers, letters = data
```

## Named Tuples

Enhanced tuples with named fields for better readability:

```python
from collections import namedtuple

# Define a named tuple class
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')  # Space-separated also works

# Create instances
p1 = Point(3, 4)
p2 = Point(x=10, y=20)
person = Person("Alice", 25, "NYC")

# Access by name or index
print(p1.x)          # 3 (by name)
print(p1[0])         # 3 (by index)
print(person.name)   # "Alice"

# Named tuples are still tuples
x, y = p1            # Unpacking works
print(len(person))   # 3

# Useful methods
print(person._fields)         # ('name', 'age', 'city')
print(p1._asdict())          # {'x': 3, 'y': 4}

# Create new instance with some fields changed
person2 = person._replace(age=26)  # Person(name='Alice', age=26, city='NYC')

# Create from iterable
data = ["Bob", 30, "LA"]
person3 = Person._make(data)
```

## Tuple vs List: When to Use Which

```python
# Use tuples for:
coordinates = (10, 20)          # Fixed structure data
rgb_color = (255, 128, 0)       # Immutable data
database_record = ("John", 30, "Engineer")  # Record-like data

# Use lists for:
shopping_cart = ["apple", "banana"]  # Data that changes
todo_items = ["task1", "task2"]      # Variable length collections
```

**Choose tuples when:**
- Data structure is fixed and won't change
- You need hashable objects (for dictionary keys or set elements)
- You want to prevent accidental modification
- Representing records or structured data
- Function returns multiple values

**Choose lists when:**
- You need to modify the collection
- Size varies during program execution
- You need list-specific methods (append, remove, etc.)

## Common Patterns

```python
# Function returning multiple values
def get_name_age():
    return "John", 30

name, age = get_name_age()

# Multiple assignment
a, b, c = 1, 2, 3

# Enumerate with unpacking
items = [("apple", 1.0), ("banana", 0.5)]
for i, (item, price) in enumerate(items):
    print(f"{i+1}. {item}: ${price}")

# Dictionary items iteration
person = {"name": "John", "age": 30}
for key, value in person.items():  # items() returns tuples
    print(f"{key}: {value}")

# Sorting by tuple elements
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
by_grade = sorted(students, key=lambda x: x[1])  # Sort by grade
by_name = sorted(students)  # Sort by name (first element)

# Using tuples as dictionary keys
locations = {
    (0, 0): "origin",
    (1, 0): "east",
    (0, 1): "north"
}
```

## Tuple Comprehensions (Generator Expressions)

While there's no true "tuple comprehension", you can use generator expressions:

```python
# Generator expression (produces generator, not tuple)
squares_gen = (x**2 for x in range(5))

# Convert to tuple if needed
squares_tuple = tuple(x**2 for x in range(5))  # (0, 1, 4, 9, 16)

# Filter and transform
numbers = (1, 2, 3, 4, 5, 6)
even_squares = tuple(x**2 for x in numbers if x % 2 == 0)  # (4, 16, 36)
```

## Performance Characteristics

```python
import timeit

# Tuples are faster to create
list_time = timeit.timeit('list([1, 2, 3, 4, 5])', number=1000000)
tuple_time = timeit.timeit('tuple([1, 2, 3, 4, 5])', number=1000000)

# Tuples use less memory
import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
print(sys.getsizeof(my_list))   # More bytes
print(sys.getsizeof(my_tuple))  # Fewer bytes

# Access time is similar for both
# But tuples can't be modified, so no append/remove overhead
```

## Advanced Usage

```python
# Tuple as function arguments (argument unpacking)
def calculate_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

point1 = (0, 0)
point2 = (3, 4)
distance = calculate_distance(*point1, *point2)  # Unpacks both tuples

# Tuple in set (because tuples are hashable)
unique_points = {(0, 0), (1, 1), (0, 0), (2, 2)}  # {(0, 0), (1, 1), (2, 2)}

# Tuple as dictionary key
cache = {}
def expensive_function(a, b, c):
    key = (a, b, c)
    if key not in cache:
        # ... expensive calculation
        cache[key] = result
    return cache[key]

# Comparing tuples (lexicographic order)
print((1, 2) < (1, 3))    # True
print((1, 2) < (2, 1))    # True
print((1, 2, 3) < (1, 2)) # False
```

## Common Gotchas

```python
# Single element tuple needs comma
single = (42)      # This is just an integer!
single = (42,)     # This is a tuple with one element
single = 42,       # This also works

# Mutable objects in tuples
point_with_list = (1, 2, [3, 4])
# point_with_list[2] = [5, 6]  # Can't do this (tuple is immutable)
point_with_list[2].append(5)   # But can modify the list inside!
# Result: (1, 2, [3, 4, 5])

# Tuple concatenation creates new tuple
original = (1, 2, 3)
extended = original + (4, 5)   # Creates new tuple, original unchanged

# Unpacking with wrong number of variables
point = (1, 2, 3)
# x, y = point  # ValueError: too many values to unpack
x, y, z = point  # Correct

# Using parentheses for grouping vs tuple creation
result = (2 + 3) * 4    # 20 (parentheses for math grouping)
result = (2 + 3,) * 4   # (5, 5, 5, 5) (tuple repetition)
```

## Memory and Performance Tips

```python
# Tuples are more memory efficient than lists
# Use tuples for large datasets that don't change

# Tuple unpacking is faster than indexing
# Good
x, y = point

# Slower
x = point[0]
y = point[1]

# Use named tuples instead of classes for simple data
# More memory efficient than full classes
Point = namedtuple('Point', 'x y')
p = Point(1, 2)

# Tuples are hashable, so they work in sets and as dict keys
# This enables powerful data structures
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    # ... adjacency list using coordinate tuples
}
```

Tuples are essential for writing clean, efficient Python code. They're perfect for immutable data, multiple return values, and anywhere you need a lightweight, ordered collection that won't change.