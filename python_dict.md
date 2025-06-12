# Complete Python Dictionaries Guide

## What Are Dictionaries?

Dictionaries are unordered, mutable collections that store key-value pairs. They're defined with curly braces `{}` and use keys to access values instead of indices.

```python
person = {"name": "John", "age": 30, "city": "New York"}
mixed = {1: "one", "two": 2, 3.14: "pi", (1, 2): "tuple key"}
empty = {}
```

## Creating Dictionaries

```python
# Direct creation
student = {"name": "Alice", "grade": 85, "subjects": ["math", "science"]}

# Using dict() constructor
from_pairs = dict([("a", 1), ("b", 2)])  # {"a": 1, "b": 2}
from_kwargs = dict(name="Bob", age=25)    # {"name": "Bob", "age": 25}

# Using dict.fromkeys()
defaults = dict.fromkeys(["a", "b", "c"], 0)  # {"a": 0, "b": 0, "c": 0}

# From two lists
keys = ["name", "age", "city"]
values = ["John", 30, "NYC"]
person = dict(zip(keys, values))
```

## Accessing Elements

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Direct access (raises KeyError if key doesn't exist)
name = person["name"]          # "John"

# Using get() (returns None or default if key doesn't exist)
age = person.get("age")        # 30
country = person.get("country")  # None
country = person.get("country", "USA")  # "USA" (default value)

# Check if key exists
has_name = "name" in person    # True
no_phone = "phone" not in person  # True
```

## Modifying Dictionaries

```python
person = {"name": "John", "age": 30}

# Add or update single key
person["city"] = "Boston"      # {"name": "John", "age": 30, "city": "Boston"}
person["age"] = 31             # Update existing key

# Delete elements
del person["city"]             # Remove key-value pair
age = person.pop("age")        # Remove and return value (31)
last_item = person.popitem()   # Remove and return last key-value pair
```

## Essential Dictionary Methods

### Adding and Updating
```python
person = {"name": "John"}

# update() - adds multiple key-value pairs
person.update({"age": 30, "city": "NYC"})
person.update([("job", "developer"), ("salary", 70000)])
person.update(country="USA", zipcode=10001)

# setdefault() - sets key only if it doesn't exist
person.setdefault("age", 25)     # Won't change existing age
person.setdefault("phone", "")   # Adds phone with empty string
```

### Getting Information
```python
person = {"name": "John", "age": 30, "city": "NYC"}

# keys(), values(), items()
keys = person.keys()           # dict_keys(['name', 'age', 'city'])
values = person.values()       # dict_values(['John', 30, 'NYC'])
items = person.items()         # dict_items([('name', 'John'), ('age', 30), ('city', 'NYC')])

# Convert to lists if needed
key_list = list(person.keys())
```

### Copying and Clearing
```python
original = {"a": 1, "b": 2}

# Shallow copy
copy1 = original.copy()
copy2 = dict(original)

# Clear all elements
original.clear()               # {}
```

## Dictionary Operations

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Merge dictionaries (Python 3.9+)
merged = dict1 | dict2         # {"a": 1, "b": 2, "c": 3, "d": 4}

# Update with merge operator
dict1 |= dict2                 # dict1 is now merged

# Length
length = len(dict1)            # Number of key-value pairs

# Comparison
dict3 = {"a": 1, "b": 2}
dict4 = {"b": 2, "a": 1}
are_equal = dict3 == dict4     # True (order doesn't matter)
```

## Dictionary Comprehensions

Create dictionaries using concise syntax:

```python
# Basic syntax: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# Transform existing dictionary
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
expensive = {fruit: price for fruit, price in prices.items() if price > 1.0}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}  # {1: "a", 2: "b", 3: "c"}

# From string
char_count = {char: word.count(char) for char in set("hello")}
```

## Iterating Over Dictionaries

```python
person = {"name": "John", "age": 30, "city": "NYC"}

# Iterate over keys (default behavior)
for key in person:
    print(key, person[key])

# Explicit iteration over keys
for key in person.keys():
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# With enumerate for index
for i, (key, value) in enumerate(person.items()):
    print(f"{i}: {key} = {value}")
```

## Nested Dictionaries

```python
# Multi-level dictionary
company = {
    "employees": {
        "john": {"age": 30, "department": "IT"},
        "jane": {"age": 25, "department": "HR"}
    },
    "departments": {
        "IT": {"budget": 100000, "head": "john"},
        "HR": {"budget": 50000, "head": "jane"}
    }
}

# Access nested values
john_age = company["employees"]["john"]["age"]  # 30

# Safely access nested values
def safe_get(dictionary, *keys):
    for key in keys:
        try:
            dictionary = dictionary[key]
        except (KeyError, TypeError):
            return None
    return dictionary

age = safe_get(company, "employees", "john", "age")  # 30
missing = safe_get(company, "employees", "bob", "age")  # None
```

## Advanced Dictionary Patterns

### Default Dictionaries
```python
from collections import defaultdict

# Automatically create missing values
dd = defaultdict(list)
dd["fruits"].append("apple")     # Creates list automatically
dd["fruits"].append("banana")    # {"fruits": ["apple", "banana"]}

# Count occurrences
counter = defaultdict(int)
text = "hello world"
for char in text:
    counter[char] += 1

# Group items
from collections import defaultdict
students = [("Alice", "Math"), ("Bob", "Science"), ("Alice", "History")]
by_student = defaultdict(list)
for name, subject in students:
    by_student[name].append(subject)
```

### Counter Dictionary
```python
from collections import Counter

# Count elements
text = "hello world"
char_count = Counter(text)       # Counter({'l': 3, 'o': 2, 'h': 1, ...})

# Most common elements
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
most_common = word_count.most_common(2)  # [('apple', 3), ('banana', 2)]

# Counter operations
c1 = Counter("hello")
c2 = Counter("world")
combined = c1 + c2               # Add counts
difference = c1 - c2             # Subtract counts
```

### Ordered Dictionaries
```python
from collections import OrderedDict

# Maintains insertion order (less relevant in Python 3.7+)
od = OrderedDict()
od["first"] = 1
od["second"] = 2

# Move to end
od.move_to_end("first")          # Moves "first" to end
od.move_to_end("second", last=False)  # Moves "second" to beginning
```

## Performance Tips

```python
# Use get() instead of checking and accessing separately
# Good
value = my_dict.get("key", default_value)

# Slower
if "key" in my_dict:
    value = my_dict["key"]
else:
    value = default_value

# Use setdefault() for initialization
# Good
my_dict.setdefault("key", []).append(item)

# Slower
if "key" not in my_dict:
    my_dict["key"] = []
my_dict["key"].append(item)

# Use items() for key-value iteration
# Good
for key, value in my_dict.items():
    process(key, value)

# Slower
for key in my_dict:
    value = my_dict[key]
    process(key, value)
```

## Common Patterns

```python
# Invert dictionary (swap keys and values)
def invert_dict(d):
    return {v: k for k, v in d.items()}

# Merge multiple dictionaries
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

# Filter dictionary
def filter_dict(d, condition):
    return {k: v for k, v in d.items() if condition(k, v)}

# Group list of dictionaries by key
def group_by_key(dict_list, key):
    groups = defaultdict(list)
    for d in dict_list:
        groups[d[key]].append(d)
    return dict(groups)

# Flatten nested dictionary
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
```

## Dictionary Views

Dictionary methods `keys()`, `values()`, and `items()` return view objects:

```python
d = {"a": 1, "b": 2, "c": 3}

keys = d.keys()      # dict_keys object
values = d.values()  # dict_values object
items = d.items()    # dict_items object

# Views are dynamic - they reflect changes
d["d"] = 4
print(len(keys))     # 4 (updated automatically)

# Set operations on views
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "c": 3}

# Find common keys
common_keys = d1.keys() & d2.keys()    # {"b"}

# Find unique keys
unique_keys = d1.keys() ^ d2.keys()    # {"a", "c"}
```

## Memory Considerations

- Dictionaries use hash tables, trading memory for speed
- Python 3.6+ dictionaries maintain insertion order
- Use `__slots__` in classes to reduce memory if you have many similar objects
- Consider `types.MappingProxyType` for read-only dictionary views

## Common Gotchas

```python
# Mutable default values in functions
def bad_function(data={}):  # DON'T DO THIS
    data["key"] = "value"
    return data

def good_function(data=None):  # DO THIS
    if data is None:
        data = {}
    data["key"] = "value"
    return data

# Modifying dictionary while iterating
d = {"a": 1, "b": 2, "c": 3}

# DON'T DO THIS
for key in d:
    if d[key] == 2:
        del d[key]  # RuntimeError!

# DO THIS
keys_to_delete = [key for key, value in d.items() if value == 2]
for key in keys_to_delete:
    del d[key]

# Using mutable objects as keys
# DON'T DO THIS
my_list = [1, 2, 3]
d = {my_list: "value"}  # TypeError! Lists aren't hashable

# DO THIS - use immutable types as keys
my_tuple = (1, 2, 3)
d = {my_tuple: "value"}  # OK

# Assuming key existence
# DON'T DO THIS
value = my_dict["key"]  # KeyError if key doesn't exist

# DO THIS
value = my_dict.get("key", "default")
# OR
if "key" in my_dict:
    value = my_dict["key"]
```

## Key Requirements

Only immutable (hashable) objects can be dictionary keys:
- ✅ Strings, numbers, tuples (with immutable elements), frozensets
- ❌ Lists, dictionaries, sets, other mutable objects

```python
# Valid keys
valid_dict = {
    "string": 1,
    42: 2,
    (1, 2): 3,
    frozenset([1, 2]): 4
}

# Invalid keys will raise TypeError
# invalid_dict = {[1, 2]: "value"}  # Lists not allowed
# invalid_dict = {{1, 2}: "value"}  # Sets not allowed
```

Dictionaries are fundamental to Python - they're fast, flexible, and used extensively throughout the language itself. Master these patterns and you'll write more efficient Python code.