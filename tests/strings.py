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

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=', ' if _ < n-1 else '\n')
        a, b = b, a + b

fibonacci(20)
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
