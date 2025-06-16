#%%
print("Reversing a String using an Extended Slicing Technique")
string = "Python Programming"
print(string[::-1]) # Outputs: gnimmargorP nohtyP

#%%
print("Counting Vowels in a Given Word")
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)
#%%
print("Counting Consonants in a Given Word")

vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character not in vowel:
        count += 1
print(count)
#%%
print("Counting the Number of Occurrences of a Character in a String")

word = "python"
character = "p"
count = 0
for letter in word:
    if letter == character:
        count += 1
print(count)

print("Using Built in Method")
word = "python"
character = "p"
count = word.count(character)
print(count)

#%%
print("Fibonacci Series")

# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=', ' if _ < n-1 else '\n')
#         a, b = b, a + b

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci(10))

#%%
print("Recursive Fibonacci")

def fibonacci_r(n):
    if (n <= 1) :
        return n
    else:
        return fibonacci_r(n-1) + fibonacci_r(n - 2)
    

print(fibonacci_r(10))
#%%
print("Finding the Maximum Number in a List")

numberList = [15, 85, 35, 89, 125]

maxNum = numberList[0]
for num in numberList:
    if maxNum < num:
        maxNum = num
print(maxNum)

print("Using Built in max():")

numberList = [15, 85, 35, 89, 125]
maxNum = max(numberList)
print(maxNum)
#%%
print("Finding the Minimum Number in a List")
numberList = [15, 85, 35, 89, 125, 2]

minNum = numberList[0]
for num in numberList:
    if minNum > num:
        minNum = num
print(minNum)

print("Using Built in min():")
numberList = [15, 85, 35, 89, 125, 2]
minNum = min(numberList)
print(minNum)
#%%
print("Converting a List into a String")

lst = ["P", "Y", "T", "H", "O", "N"]
string = ''.join(lst)

print(string)
print(type(string))

#%%
print("Adding Two List Elements Together")

lst1 = [1, 2, 3]
lst2 = [4, 5, 6] 

res_lst = [] 
for i in range(0, len(lst1)):
    res_lst.append(lst1[i] + lst2[i]) 
print(res_lst)

print("Another approach:")
a = [1, 2, 3]
b = [4, 5, 6]

c = [x + y for x, y in zip(a, b)]
print(c)

# %%
print("zip() pairs up elements from multiple iterables (lists, tuples, etc.) position by position:\n")

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print("lst1:", lst1)
print("lst2:", lst2)
zipped = zip(lst1, lst2)
# Creates: (1,4), (2,5), (3,6)
print("\nzip type is",type(zipped))
for a, b in zipped:
    print(f"{a} + {b} = {a + b}")

print("\nMultiple lists:")  
names = ['Alice', 'Bob', 'Charlie']
print("names:", names)
ages = [25, 30, 35]
print("ages:", ages)
cities = ['NYC', 'LA', 'Chicago']
print("cities:", cities)

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

print("\nDifferent lengths:")
list1 = [1, 2, 3, 4]
list2 = [10, 20]

print("list1:", list1)
print("list2:", list2)

for a, b in zip([1, 2, 3, 4], [10, 20]):
    print(f"{a} + {b} = {a + b}")
# Output: [(1, 10), (2, 20)]
print("Stops at shortest list")

# %%
print("\nComparing Two Strings for Anagrams")

print("\nBasic Approach")

str1 = "Listen"
print("str1 =", str1)
str2 = "Silent"
print("str2 =", str2)

str1 = list(str1.upper())
str2 = list(str2.upper())
str1.sort() # Uses TimeSort
str2.sort()

print("Sorted str1 =", str1)
print("Sorted str2 =", str2)

if(str1 == str2):
    print("True")
else:
    print("False")

#%%
print("\nChecking for Palindrome Using Extended Slicing Technique")

str1 = "Kayak".lower()
print("str1 =", str1)
str2 = "kayak".lower()
print("str2 =", str2)


if(str1 == str2[::-1]):
    print("if(str1 == str2[::-1]): True")
else:
    print("if(str1 == str2[::-1]):False")
    
# %%
print("\nChecking for Palindrome Using Extended Slicing Technique")

string = "P r ogramm in g "
print(f"string =\"{string}\"")
print("string.count(' ') =",string.count(' '))

# %%
print("\nCounting Digits, Letters, and Spaces in a String")

# Importing Regular Expressions Library
import re
print("import re")

name = 'Python is 1'
print("name = ", name)

digitCount = re.sub("[^0-9]", "", name)
print("digitCount =", digitCount)
letterCount = re.sub("[^a-zA-Z]", "", name)
print("letterCount =", letterCount)
spaceCount = re.findall("[ \n]", name)
print("spaceCount =", spaceCount)

print("len(digitCount) =", len(digitCount))
print("len(letterCount) =", len(letterCount))
print("len(spaceCount) =", len(spaceCount))

# %%
print("\nCounting Special Characters in a String")
print("spChar = \"!@#$%^&*()\"")
spChar = "!@#$%^&*()"

count = re.sub('[\w]+', '', spChar)
print(len(count))

# %%
print("\nRemoving All Whitespace in a String")
print("string = \"C O D E\"")
string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, '', string)
print(result)
# %%
print("\nBuilding a Pyramid in Python")

floors = 10
h = 2*floors-1
for i in range(1, 2*floors, 2):
    print('{:^{}}'.format('*'*i, h))

# %%
print("\nRandomizing the Items of a List in Python")
print("from random import shuffle\n")
from random import shuffle

lst = ['Python', 'is', 'Easy']
print("lst before shuffle:",lst)
shuffle(lst)
print("lst after shuffle:",lst)

# %%
print("\nFind the Largest Element in a List")

def find_largest_element(lst):
    return max(lst)

# Example usage:
print(find_largest_element([1, 2, 3, 4, 5]))

# %%
print("\nRemove Duplicates from a List:\n")

def remove_duplicates(lst):
    return list(set(lst))

# Example usage:
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# %%
print("\nFactorial of a Number:\n")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("def factorial(n):\n\tif n == 0:\n\t\treturn 1\n\treturn n * factorial(n - 1)")

# Example usage:
print("\nfactorial(5) =", factorial(5))

# %%
print("\nMerge Two Sorted Lists:\n")

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

print("def merge_sorted_lists(lst1, lst2):\n\treturn sorted(lst1 + lst2)\n")
# Example usage:

print("merge_sorted_lists([1, 3, 5], [2, 4, 6]) =", merge_sorted_lists([1, 3, 5], [2, 4, 6]))
# %%
print("\nFind the First Non-Repeating Character:\n")

def first_non_repeating_character(s):
    for i in s:
        if s.count(i) == 1:
            return i  
    return None

print("def first_non_repeating_character(s):\n\tfor i in s:\n\t\tif s.count(i) == 1:\n\t\t\treturn i\n\treturn None")

# Example usage:
print("\nfirst_non_repeating_character(\"swiss\") =", first_non_repeating_character("swiss"))
# %%

