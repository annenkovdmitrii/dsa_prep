# Hash Tables

# Hashing is a process that takes input data of any size and converts it 
# into a fixed-size string of characters (called a hash or hash value) 
# using a mathematical function called a hash function.


# Built-in hash table in Python is a Dict. {} or set()

# Charachteristics:
# One-way
# Deterministic 

# Collision Method:
# Chaining (Separate Chaining)

# Each bucket contains a linked list (or dynamic array) of all elements that hash to that location
# Simple to implement, handles high load factors well
# Extra memory overhead for pointers/references

class HashTable:
    def __init__(self, size = 7): # set the default size to be 7 elements
        self.data_map = [None] * size
        
    def __hash(self, key):
        # ord(letter) - Converts each character to its ASCII number (A=65, B=66, a=97, etc.)
        # *23 - Multiplies by 23 (a prime number chosen to spread out hash values and reduce collisions)
        # my_hash + - Adds to the running total from previous characters
        # % len(self.data_map) - Modulo operation keeps the result within array bounds (0 to 6 for size 7)
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map) # ord() retruns ASCII numerical value for each letter
        return my_hash