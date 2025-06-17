#%% Problem: Given an array of integers nums, 
# find all the duplicates in the array using a hash table (dictionary).

# Input:
# A list of integers nums.

# Output:
# A list of integers representing the numbers in the input array 
# nums that appear more than once. If no duplicates are found 
# in the input array, return an empty list [].
def find_duplicates(nums):
    # if list is empty
    if nums == []:
        return []
    mydict = {}
    for n in nums:
        mydict[n] = 1 + mydict.get(n, 0)
    
    dupl = []
    for key, value in  mydict.items():
        if value > 1:
            dupl.append(key)
    return dupl


#%% Testing find_duplicates

print ("\n Testing on [1, 2, 3, 4, 5]:" , find_duplicates([1, 2, 3, 4, 5]) )
print ("\n Testing on [1, 1, 2, 2, 3]:" , find_duplicates([1, 1, 2, 2, 3]) )
print ("\n Testing on [1, 1, 1, 1, 1]:" , find_duplicates([1, 1, 1, 1, 1]) )
print ("\n Testing on [1, 2, 3, 3, 3, 4, 4, 5]:" , find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ("\n Testing on [1, 1, 2, 2, 2, 3, 3, 3, 3]:" , find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ("\n Testing on [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]:" , find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ("\n Testing on []:", find_duplicates([]) )

# %%
