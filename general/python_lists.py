#%% List Creation

# Direct creation
fruits = ["apple", "banana", "cherry"]

# Using list() constructor
numbers = list(range(5))  # [0, 1, 2, 3, 4]
chars = list("hello")     # ['h', 'e', 'l', 'l', 'o']

# List multiplication
zeros = [0] * 5           # [0, 0, 0, 0, 0]

#%% List Access

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

#%% Modifying Lists
fruits = ["apple", "banana", "cherry"]

# Change single element
fruits[0] = "apricot"     # ["apricot", "banana", "cherry"]

# Change multiple elements
fruits[1:3] = ["blueberry", "coconut"]  # ["apricot", "blueberry", "coconut"]

# Delete elements
del fruits[0]             # ["blueberry", "coconut"]
del fruits[1:3]

#%% Removing Elements
fruits = ["apple", "banana", "cherry", "banana"]

# remove() - removes first occurrence
fruits.remove("banana")    # ["apple", "cherry", "banana"]

# pop() - removes and returns element
last = fruits.pop()        # Returns "banana", list becomes ["apple", "cherry"]
first = fruits.pop(0)      # Returns "apple", list becomes ["cherry"]

# clear() - removes all elements
fruits.clear()             # []

#%% Finding Elements (Look up)
numbers = [1, 2, 3, 2, 4]

# index() - returns index of first occurrence
pos = numbers.index(2)     # 1

# count() - counts occurrences
count = numbers.count(2)   # 2

# Check if element exists
exists = 3 in numbers      # True
not_exists = 5 not in numbers  # True

#%% Sorting and Reversing
numbers = [3, 1, 4, 1, 5]

# sort() - sorts in place
numbers.sort()             # [1, 1, 3, 4, 5]
numbers.sort(reverse=True) # [5, 4, 3, 1, 1]

# sorted() - returns new sorted list
original = [3, 1, 4]
new_sorted = sorted(original)  # original unchanged

# reverse() - reverses in place
numbers.reverse()          # Reverses current order

#%% List Operations

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

#%% List Comprehension

# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
print(squares)

# Transform strings
words = ["hello", "world"]
upper_words = [word.upper() for word in words]  # ["HELLO", "WORLD"]
print(upper_words)

# Nested comprehensions
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

#%% Copying Lists

original = [1, 2, [3, 4]]

# Shallow copy (copies list but not nested objects)
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# Deep copy (copies everything including nested objects)
import copy
deep_copy = copy.deepcopy(original)

#%% Iterating Over Lists

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
    
#%% Nested Lists

# 2D list (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access elements
element = matrix[1][2]  # 6 (row 1, column 2)

# Modify elements
matrix[0][0] = 10       # [[10, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4, 5, 6]

#%% Performance Tips

# Use list comprehensions instead of loops when possible
# Good
squares = [x**2 for x in range(1000)]

# Slower
squares = []
for x in range(1000):
    squares.append(x**2)

my_list = []
# Use extend() instead of multiple append() calls
# Good
my_list.extend([1, 2, 3])

# Slower
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Preallocate size if known
my_list = [None] * 1000  # Then assign values

# Common Patterns
#%% Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

#%% Chunk list into smaller lists
def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

#%% Find all indices of an element
def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

#%% Rotate list
def rotate_list(lst, n):
    return lst[n:] + lst[:n]

#%%
test_list = [4, 9, 22, 2, 6, 3, 3, 4, 78, 12, 33, 1, 0, 8, 99]

print(rotate_list(test_list, 2))
#%%
print(find_all_indices(test_list, 3))
    
# %%
print(chunk_list(test_list, 2))

#%%
print(remove_duplicates(test_list))
# %% Common Gotchas
# 
# # Mutable default arguments
def bad_function(lst=[]):  # DON'T DO THIS
    lst.append(1)
    return lst

def good_function(lst=None):  # DO THIS
    if lst is None:
        lst = []
    lst.append(1)
    return lst
# %%
print(bad_function())
print(bad_function())
print(bad_function())
print(bad_function())
print(bad_function())
#%%
print(good_function())
print(good_function()) 
print(good_function()) 
print(good_function()) 

#%% Shallow copy issues
original = [[1, 2], [3, 4]]
print("original:", original)
copy = original.copy()
copy[0][0] = 99  # This changes original[0][0] too!

print("now original:",original)
print("copy",copy)

print("\noriginal is copy =", original is copy)
print("original[0] is copy[0] =", original[0] is copy[0])
print("original[1] is copy[1] =", original[1] is copy[1])

#%% List multiplication with mutable objects
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("original matrix:", matrix)
matrix = [[0] * 3] * 3  # DON'T DO THIS - all rows are the same object
matrix[0][0] = 99
print("\nmatrix = [[0] * 3] * 3 AND matrix[0][0] = 99:", matrix)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[0] * 3 for _ in range(3)]  # DO THIS
matrix[0][0] = 99
print("\nmatrix = [[0] * 3 for _ in range(3)] AND matrix[0][0] = 99", matrix)
# %%
def addToList(a): 
    a += [10] 
b = [10, 20, 30, 40] 
addToList(b) 
print(len(b))
print(b)
# %%
a = [10, 20, 30, 40, 50] 
b = [1, 2, 3, 4, 5] 


subtracted = list()
for a, b in zip(a, b):
    item = a -b
    subtracted.append(item)

print(subtracted)

# %%
li = ['a', 'b', 'c', 'd', 'e'] 
print(li[10:] )
# print(li[10])  <-- ERROR
# %%
li = ['a', 'b', 'c'] * -3
print(li)

# An expression list[listelements]*N where N is an integer appends N copies 
# of list elements in the original list. If N is a negative integer or 0 output 
# will be an empty list else if N is positive list elements will be 
# added N times to the original list.
# %%
li = [2, 3, 9] 
li = [[x for x in[li]] for x in range(3)] 
print (li)
# [x for x in[li] returns a new list copying the values in the list li 
# and the outer for statement prints the newly created list 3 times.
# %%
a = [x for x in range(5)] 
b = [x for x in range(7) if x in a and x%2==0] 
print(b) 

# This statement checks whether the value lies in list data and 
# if it does whether it’s divisible by 2. It does so for x in (0, 7).
# %%
a = ['Geeks', 'for', 'Geeks'] 
b = [i[0].upper() for i in a] 
print(b) 
# The variable i is used to iterate over each element in list temp. 
# i[0] represent the character at 0th index of i and .upper() function 
# is used to capitalize the character present at i[0].
# %%
a = 'Geeks 22536 for 445 Geeks'
b = [x for x in (int(x) for x in a if x.isdigit()) if x%2 == 0] 
print(b) 

# Nested list comprehension
# Inner list is [2, 2, 5, 3, 6, 4, 4, 5] - skips non-digits and converts digits to int
# So the outter list is [2, 2, 6, 4, 4] - only appends even integers from list above
# %%
a = [x for x in (x for x in 'Geeks 22966 for Geeks' if x.isdigit()) if
(x in ([x for x in range(20)]))] 
print(a) 

# Step 1: Inner generator (x for x in 'Geeks 22966 for Geeks' if x.isdigit())

# Extracts digit characters from the string
# From 'Geeks 22966 for Geeks', the digits are: '2', '2', '9', '6', '6'
# These are strings, not integers

# Step 2: The condition [x for x in range(20)]

# Creates a list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# These are integers

# Step 3: The filter condition if (x in ([x for x in range(20)]))

# Checks if each digit string is in the list of integers
# '2' (string) is not equal to 2 (integer)
# '9' (string) is not equal to 9 (integer)
# etc.

# Since strings are never equal to integers, none of the digit strings are found in the integer list.
# Output: [] (empty list)
# The code has a type mismatch between string digits and integer values.
# %%
a = []
a.append([1, [2, 3], 4])
print(a)
a.extend([7, 8, 9])
print(a)
print(a[0][1][1] + a[2])


# %%
li = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True] 
val1, val2 = 0,'' 
for x in li: 
	if(type(x) == int or type(x) == float): 
		val1 += x 
	elif(type(x) == str): 
		val2 += x 
	else: 
		break
print(val1, val2) 

# %%
a = [1, 2, 3, 4] 
b = a 
c = a.copy() 
d = a
a[0] = [5] 
print(a, b, c, d) 
# In the given code, b is a shallow copy of a, meaning it references the same list as a, 
# while c and d are not deep copies, as c is a shallow copy created using .copy() and d is a 
# reference to a. The modification a[0] = [5] replaces the first element of a with the list [5], 
# which is also reflected in b and d.

# %%
li = [1, 3, 5, 7, 9] 
print(li.pop(-3), end = ' ') 
# %%
nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 

pos = nameList.index("GeeksforGeeks") 

print (pos * 3)

# %%
