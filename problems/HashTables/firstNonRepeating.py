#%% First Non-Repeating Character
# first_non_repeating_char(string) that finds the first 
# non-repeating character in the given string using a hash table (dictionary). 
# If there is no non-repeating character in the string, the function should return None.

# given a string of lowercase letters.
def first_non_repeating_char(stringIn):
    mydict = {}
    for i in range(len(stringIn)):
        mydict[stringIn[i]] = 1 + mydict.get(stringIn[i], 0)

    for key, value in mydict.items():
        if value == 1:
            return key
    return None
#%% Testing

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
#%% Official Solution
def first_non_repeating_char_(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None
#%%