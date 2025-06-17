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


# Big O

# Hash method: O(1)
# Setting an item: O(1)
# Getting an item: O(1) this is assumed given a 'good' distribution 

class HashTable:
    def __init__(self, size = 7): # set the default size to be 7 elements, prime number reduces collisions and increases ramdomnes
        self.data_map = [None] * size
        
    def __hash(self, key):
        # ord(letter) - Converts each character to its ASCII number (A=65, B=66, a=97, etc.)
        # *23 - Multiplies by 23 (a prime number chosen to spread out hash values and reduce collisions)
        # my_hash + - Adds to the running total from previous characters
        # % len(self.data_map) - Modulo operation keeps the result within array bounds (0 to 6 for size 7)
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map) 
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
            
    def set_item(self, key, value):
        index = self.__hash(key) # this will compute the address
        if self.data_map[index] == None:
            self.data_map[index] = []  # initialize the empty set if it didnt exist before
        self.data_map[index].append([key, value]) # add the key - value pair to the end of the list
        
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])): # going through the list within at the index and check if we have a match with key
                if self.data_map[index][i][0] == key: # i is the list within list within list, where 0 stands for the key
                    return self.data_map[index][i][1] # return the value in the key pair list
        return None # if the key wasn't found
                
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)): # loops over indecies (main list)
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])): # iterating within a list at index i (if there is something in there)
                    all_keys.append(self.data_map[i][j][0]) # adding all the keys within list j that is within list i
        return all_keys            
        
        
# Example usage
if __name__ == "__main__":
    print("Testing HashTable Class")
    my_hash_table = HashTable()
    
    print("\nTesting Set_item Method in the HashTable:")
    my_hash_table.set_item('bolts',1400)
    my_hash_table.set_item('washers',50)
    my_hash_table.set_item('lumber',70)
    my_hash_table.set_item('nails',2000)
    my_hash_table.set_item('cogs',600)
    my_hash_table.set_item('screws', 850)
    my_hash_table.set_item('drill', 1)
    my_hash_table.set_item('hammer', 3)
    my_hash_table.set_item('saw', 2)
    my_hash_table.set_item('pliers', 4)
    
    # print("\nAdded edge cases")
    my_hash_table.set_item('a', 999)        # Single character
    my_hash_table.set_item('z', 111)        # Different single character
    my_hash_table.set_item('toolbox', 25)   # Longer key
    my_hash_table.set_item('workshop', 100) # Another longer key
    
    # print("\nPotential collision testing (keys that might hash to same index)")
    my_hash_table.set_item('nuts', 300)
    my_hash_table.set_item('pins', 150)
    my_hash_table.set_item('tape', 45)
    
    print("\nDifferent data types as values")
    my_hash_table.set_item('brand', 'DeWalt')
    my_hash_table.set_item('price', 99.99)
    my_hash_table.set_item('instock', True)

    
    print("\nFinal HashTable state:")
    my_hash_table.print_table()
    
    
    print("\nTesting Get_item Method:")
    
    print('Looking for bolts:',my_hash_table.get_item('bolts'))
    print('Looking for washers:',my_hash_table.get_item('washers'))
    print('Looking for lumber:',my_hash_table.get_item('lumber'))
    print('Looking for caps:',my_hash_table.get_item('caps'))
    
    print("\nTesting Keys Method:")
    print(my_hash_table.keys())