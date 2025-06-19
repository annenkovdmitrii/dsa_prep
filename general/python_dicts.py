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

# setdefault() - sets key only if it doesn't exist
person.setdefault("age", 25)     # Won't change existing age
person.setdefault("phone", "")   # Adds phone with empty string
print(person)
#%%