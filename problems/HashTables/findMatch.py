#%% Naive approach 
# O(n^2)
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
            
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))

#%% Hash Table Approach
# O(n)

def better_item_in_common(list1, list2):
    # using a dict
    dict1 = {}
    for i in list1:
        dict1[i] = True
    # not nested for loops, but one after another
    for j in list2:
        if j in dict1:
            return True
        
    return False

print(better_item_in_common(list1, list2))
# %% Hash Set Approach

def great_item_in_common(list1, list2):
    myset = set()
    
    for i in list1:
        myset.add(i)
        
    for j in list2:
        if j in myset:
            return True
    return False

print(great_item_in_common(list1, list2))

# %%
