#%% Creating Dictionaries

# Direct creation
student = {"name": "Alice", "grade": 85, "subjects": ["math", "science"]}

# Using dict() constructor
from_tuples = dict([("a", 1), ("b", 2)])  # {"a": 1, "b": 2}
from_kwargs = dict(name="Bob", age=25)    # {"name": "Bob", "age": 25}

# Using dict.fromkeys()
defaults = dict.fromkeys(["a", "b", "c"], 0)  # {"a": 0, "b": 0, "c": 0}

# From two lists
keys = ["name", "age", "city"]
values = ["John", 30, "NYC"]
person = dict(zip(keys, values))

#%%Accessing Elements

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

#%% Modifying Dictionaries

person = {"name": "John", "age": 30}

# Add or update single key
person["city"] = "Boston"      # {"name": "John", "age": 30, "city": "Boston"}
person["age"] = 31             # Update existing key

# Delete elements
del person["city"]             # Remove key-value pair
age = person.pop("age")        # Remove and return value (31)
last_item = person.popitem() 
#%% Adding and Updating

person = {"name": "John"}
print(person)
# update() - adds multiple key-value pairs
person.update({"age": 30, "city": "NYC"})
person.update([("job", "developer"), ("salary", 70000)])
person.update(country="USA", zipcode=10001)
print(person)
# setdefault() - sets key only if it doesn't exist
person.setdefault("age", 25)     # Won't change existing age
person.setdefault("phone", "")   # Adds phone with empty string
print(person)
#%% More setdefault() usecases
counts = {}
for char in "hello":
    counts.setdefault(char, 0)
    counts[char] += 1
print(counts)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#%% Getting Information
person = {"name": "John", "age": 30, "city": "NYC"}
print("original dict:",person)
# keys(), values(), items()
keys = person.keys()           # dict_keys(['name', 'age', 'city'])
print("keys:", keys)
values = person.values()       # dict_values(['John', 30, 'NYC'])
print("values:",values)
items = person.items()         # dict_items([('name', 'John'), ('age', 30), ('city', 'NYC')])
print("items:", items)

# Convert to lists if needed
key_list = list(person.keys())
print("key_list:",key_list)
# %%
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

common_keys = dict1.keys() & dict2.keys()  # {'b'}
print("dict1.keys() & dict2.keys() =", common_keys)

all_keys = dict1.keys() | dict2.keys()     # {'a', 'b', 'c'}
print("dict1.keys() | dict2.keys() =", all_keys)

# %% Copying and Clearing
# A shallow copy creates a new object, but the elements inside 
# still reference the same objects as the original.

# This means:
# Changes to the container itself (adding/removing elements) don't affect the original
# Changes to mutable elements within the container affect both the original and the copy

original = {"a": 1, "b": 2}
print("original =", original)
# Shallow copy
copy1 = original.copy()
print("original.copy() =",copy1)

copy2 = dict(original)
print("dict(original) =",copy2)
# Clear all elements
original.clear()   # {}
print("\nAfter original.clear():")

print("copy1 =", copy1)
print("copy2 =", copy2)
# %% Dictionary Operations

dict1 = {"a": 1, "b": 2}
print(dict1)
dict2 = {"c": 3, "d": 4}
print(dict2)

# Merge dictionaries (Python 3.9+)
merged = dict1 | dict2         # {"a": 1, "b": 2, "c": 3, "d": 4}
print("dict1 | dict2  =",merged)

# Update with merge operator
dict1 |= dict2                 # dict1 is now merged
print("dict1 |= dict2 -->", dict1)
# Length
length = len(dict1)            # Number of key-value pairs

# Comparison
dict3 = {"a": 1, "b": 2}
print(dict3)
dict4 = {"b": 2, "a": 1}
print(dict4)
are_equal = dict3 == dict4     # True (order doesn't matter)
print("dict3 == dict4 =", are_equal)
# %% Create dictionaries using concise syntax:

# Basic syntax: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(squares)
# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)

# Transform existing dictionary
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
print("prices =", prices)
expensive = {fruit: price for fruit, price in prices.items() if price > 1.0}
print('{fruit: price for fruit, price in prices.items() if price > 1.0} =', expensive)
# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
print(original)
swapped = {v: k for k, v in original.items()}  # {1: "a", 2: "b", 3: "c"}
print('{v: k for k, v in original.items()} =', swapped)
# From string
word = "hello world"
print(word)
char_count = {char: word.count(char) for char in set("hello")}
print('{char: word.count(char) for char in set("hello")} =', char_count)  # {'e': 1, 'h': 1, 'l': 3, 'o': 2}
# %% Iterating Over Dictionaries

person = {"name": "John", "age": 30, "city": "NYC"}
print(person)

print("\nIterate over keys (default behavior)")
for key in person:
    print(key, person[key])

print("\nExplicit iteration over keys")
for key in person.keys():
    print(key)

print("\nIterate over values")
for value in person.values():
    print(value)

print("\nIterate over key-value pairs")
for key, value in person.items():
    print(f"{key}: {value}")

print("\nWith enumerate for index")
for i, (key, value) in enumerate(person.items()):
    print(f"{i}: {key} = {value}")
