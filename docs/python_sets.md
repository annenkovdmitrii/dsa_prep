# Complete Python Sets Guide

## What Are Sets?

Sets are unordered, mutable collections of unique elements. They're defined with curly braces `{}` or the `set()` function. Sets automatically eliminate duplicates and are optimized for membership testing and set operations.

```python
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, (1, 2)}  # Can contain different hashable types
empty = set()  # Note: {} creates an empty dict, not set
```

## Creating Sets

```python
# Direct creation with curly braces
colors = {"red", "green", "blue"}

# Using set() constructor
from_list = set([1, 2, 3, 2, 1])      # {1, 2, 3} - duplicates removed
from_string = set("hello")            # {'h', 'e', 'l', 'o'} - duplicates removed
from_tuple = set((1, 2, 3))           # {1, 2, 3}

# Remove duplicates from list
original_list = [1, 2, 2, 3, 3, 4]
unique_items = list(set(original_list))  # [1, 2, 3, 4] (order may vary)

# Empty set
empty = set()  # {} creates empty dict, not set!
```

## Set Operations

Sets support mathematical set operations:

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (all elements from both sets)
union1 = set1 | set2              # {1, 2, 3, 4, 5, 6}
union2 = set1.union(set2)         # Same result

# Intersection (common elements)
intersection1 = set1 & set2       # {3, 4}
intersection2 = set1.intersection(set2)  # Same result

# Difference (elements in first set but not second)
difference1 = set1 - set2         # {1, 2}
difference2 = set1.difference(set2)  # Same result

# Symmetric difference (elements in either set, but not both)
sym_diff1 = set1 ^ set2           # {1, 2, 5, 6}
sym_diff2 = set1.symmetric_difference(set2)  # Same result

# Check relationships
is_subset = {1, 2} <= set1        # True
is_superset = set1 >= {1, 2}      # True
is_disjoint = set1.isdisjoint({7, 8})  # True (no common elements)
```

## Essential Set Methods

### Adding Elements
```python
fruits = {"apple", "banana"}

# add() - adds single element
fruits.add("cherry")              # {"apple", "banana", "cherry"}
fruits.add("apple")               # No change (already exists)

# update() - adds multiple elements
fruits.update(["date", "fig"])    # Add from list
fruits.update({"grape", "kiwi"})  # Add from set
fruits.update("mango")            # Add each character: 'm', 'a', 'n', 'g', 'o'
```

### Removing Elements
```python
fruits = {"apple", "banana", "cherry"}

# remove() - removes element (raises KeyError if not found)
fruits.remove("banana")           # {"apple", "cherry"}
# fruits.remove("orange")         # KeyError!

# discard() - removes element (no error if not found)
fruits.discard("apple")           # {"cherry"}
fruits.discard("orange")          # No error, set unchanged

# pop() - removes and returns arbitrary element
item = fruits.pop()               # Returns and removes random element
# empty_set.pop()                 # KeyError on empty set

# clear() - removes all elements
fruits.clear()                    # set()
```

### Set Comparisons and Tests
```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {6, 7, 8}

# Subset/superset tests
print(set1.issubset(set2))        # True
print(set1 <= set2)               # True (same as issubset)
print(set1 < set2)                # True (proper subset)

print(set2.issuperset(set1))      # True
print(set2 >= set1)               # True (same as issuperset)
print(set2 > set1)                # True (proper superset)

# Disjoint test (no common elements)
print(set1.isdisjoint(set3))      # True

# Membership testing (very fast)
print(2 in set1)                  # True
print(10 not in set2)             # True
```

## Set Comprehensions

Create sets using concise syntax:

```python
# Basic syntax: {expression for item in iterable}
squares = {x**2 for x in range(5)}     # {0, 1, 4, 9, 16}

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}  # {0, 4, 16, 36, 64}

# From string (unique characters)
unique_chars = {char.lower() for char in "Hello World"}  # {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

# Transform existing set
words = {"apple", "banana", "cherry"}
lengths = {len(word) for word in words}  # {5, 6} - unique lengths

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
all_elements = {element for row in matrix for element in row}  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

## Iterating Over Sets

```python
colors = {"red", "green", "blue"}

# Basic iteration (order is not guaranteed)
for color in colors:
    print(color)

# With enumerate (if you need index)
for i, color in enumerate(colors):
    print(f"{i}: {color}")

# Convert to sorted list for ordered iteration
for color in sorted(colors):
    print(color)  # Prints in alphabetical order

# Iterate over multiple sets
sizes = {"small", "medium", "large"}
# Note: zip may not align properly since sets are unordered
for color, size in zip(sorted(colors), sorted(sizes)):
    print(f"{color} {size}")
```

## Frozensets (Immutable Sets)

Frozensets are immutable versions of sets that can be used as dictionary keys or set elements:

```python
# Create frozenset
fs1 = frozenset([1, 2, 3])
fs2 = frozenset("hello")           # frozenset({'h', 'e', 'l', 'o'})

# Frozensets support all non-mutating set operations
fs3 = frozenset([2, 3, 4])
union = fs1 | fs3                  # frozenset({1, 2, 3, 4})
intersection = fs1 & fs3           # frozenset({2, 3})

# Can be used as dictionary keys or set elements
nested_sets = {
    frozenset([1, 2]): "first",
    frozenset([3, 4]): "second"
}

set_of_sets = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([1, 2])              # Duplicate, will be ignored
}

# Cannot modify frozensets
# fs1.add(4)                       # AttributeError
```

## Performance Characteristics

Sets are implemented as hash tables, making them very fast for certain operations:

```python
import timeit

# Membership testing - sets are much faster than lists
large_list = list(range(10000))
large_set = set(range(10000))

# Fast in sets
list_time = timeit.timeit('9999 in large_list', globals=globals(), number=10000)
set_time = timeit.timeit('9999 in large_set', globals=globals(), number=10000)

print(f"List: {list_time:.6f} seconds")
print(f"Set: {set_time:.6f} seconds")  # Much faster!

# Remove duplicates - sets are efficient
def remove_duplicates_list(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

def remove_duplicates_set(items):
    return list(set(items))

# The set method is much faster for large datasets
```

## Common Patterns

```python
# Remove duplicates while preserving some order (Python 3.7+)
def ordered_unique(sequence):
    return list(dict.fromkeys(sequence))

# Find common elements across multiple sets
def find_common(*sets):
    if not sets:
        return set()
    result = sets[0]
    for s in sets[1:]:
        result &= s
    return result

# Find elements that appear in exactly one set
def unique_to_one_set(*sets):
    all_elements = set()
    for s in sets:
        all_elements |= s
    
    result = set()
    for element in all_elements:
        count = sum(1 for s in sets if element in s)
        if count == 1:
            result.add(element)
    return result

# Group items by property
def group_by_property(items, key_func):
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = set()
        groups[key].add(item)
    return groups

# Power set (all subsets)
def power_set(s):
    from itertools import combinations
    result = set()
    for r in range(len(s) + 1):
        for combo in combinations(s, r):
            result.add(frozenset(combo))
    return result
```

## Set Operations with Multiple Sets

```python
sets = [
    {1, 2, 3},
    {2, 3, 4},
    {3, 4, 5},
    {4, 5, 6}
]

# Union of all sets
all_elements = set().union(*sets)  # {1, 2, 3, 4, 5, 6}

# Intersection of all sets
common = sets[0].intersection(*sets[1:])  # {3} if using example above

# Elements that appear in at least 2 sets
from collections import Counter
element_counts = Counter()
for s in sets:
    element_counts.update(s)

in_multiple = {elem for elem, count in element_counts.items() if count >= 2}
```

## Advanced Usage

```python
# Using sets for algorithm optimization
def has_duplicate_characters(string):
    return len(string) != len(set(string))

# Fast way to check if two sequences have common elements
def have_common_elements(seq1, seq2):
    return bool(set(seq1) & set(seq2))

# Filter unique items from multiple sources
def merge_unique(*iterables):
    result = set()
    for iterable in iterables:
        result.update(iterable)
    return result

# Set-based filtering
def filter_by_whitelist(items, whitelist):
    whitelist_set = set(whitelist)
    return [item for item in items if item in whitelist_set]

def filter_by_blacklist(items, blacklist):
    blacklist_set = set(blacklist)
    return [item for item in items if item not in blacklist_set]

# Symmetric operations
def find_differences(set1, set2):
    only_in_first = set1 - set2
    only_in_second = set2 - set1
    in_both = set1 & set2
    return only_in_first, only_in_second, in_both
```

## Memory Considerations

```python
# Sets use more memory than lists for small collections
# But provide O(1) lookup vs O(n) for lists

# For large datasets with frequent membership testing, sets are better
# For small datasets where order matters, lists might be better

# Sets automatically resize, so they may use more memory than needed
# Consider frozensets for immutable data to save some memory

import sys
my_list = [1, 2, 3, 4, 5]
my_set = {1, 2, 3, 4, 5}

print(f"List size: {sys.getsizeof(my_list)} bytes")
print(f"Set size: {sys.getsizeof(my_set)} bytes")  # Usually larger
```

## Common Gotchas

```python
# Empty set vs empty dict
empty_dict = {}          # This is a dictionary!
empty_set = set()        # This is a set

# Sets only contain hashable elements
# valid_set = {1, 2, 3, "hello", (1, 2)}  # OK
# invalid_set = {1, 2, [3, 4]}            # TypeError! Lists aren't hashable

# Set order is not guaranteed (though Python 3.7+ maintains insertion order)
my_set = {3, 1, 4, 1, 5}
print(my_set)  # Order may vary, duplicates removed

# Modifying set while iterating
my_set = {1, 2, 3, 4, 5}

# DON'T DO THIS
# for item in my_set:
#     if item % 2 == 0:
#         my_set.remove(item)  # RuntimeError!

# DO THIS
to_remove = {item for item in my_set if item % 2 == 0}
my_set -= to_remove

# OR THIS
my_set = {item for item in my_set if item % 2 != 0}

# Using mutable objects as set elements
# my_set = {[1, 2], [3, 4]}  # TypeError! Lists aren't hashable

# Use frozensets or tuples instead
my_set = {frozenset([1, 2]), frozenset([3, 4])}  # OK
my_set = {(1, 2), (3, 4)}                        # Also OK

# Set comprehension with side effects
# Be careful with functions that have side effects in set comprehensions
# The function might be called multiple times or not at all for duplicates
```

## When to Use Sets

**Use sets when:**
- You need to eliminate duplicates
- You need fast membership testing (`item in collection`)
- You're doing mathematical set operations (union, intersection, etc.)
- Order doesn't matter
- You need to find unique elements across multiple collections

**Don't use sets when:**
- You need to maintain order (use list or dict keys in Python 3.7+)
- You need to store mutable objects (lists, dicts, other sets)
- You need indexed access
- You're dealing with small collections where the overhead isn't worth it

## Set vs Other Data Structures

```python
# Set vs List for membership testing
# Set: O(1) average case
# List: O(n) average case

# Set vs Dict for unique keys
# Both are similar, but sets are cleaner for just tracking existence

# Use set when you only care about presence
visited = set()
visited.add(item)

# Use dict when you need to store associated data
cache = {}
cache[item] = result
```

Sets are powerful tools for efficient data processing, especially when dealing with uniqueness, membership testing, and mathematical set operations. They're essential for writing performant Python code that deals with collections of unique items.