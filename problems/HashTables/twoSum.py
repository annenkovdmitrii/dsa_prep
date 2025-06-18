#%% Problem:
# Given an array of integers nums and a target integer target, 
# find the indices of two numbers in the array that add up to the target.

# The main challenge here is to implement this function 
# in one pass through the array. This means you should not 
# iterate over the array more than once. Therefore, your solution
# should have a time complexity of O(n), where n is the number of elements in nums.

# Input:
# A list of integers nums .
# A target integer target.

# Output:
# A list of two integers representing the indices of 
# the two numbers in the input array nums that add up to the target. 
# If no two numbers in the input array add up to the target, return an empty list [].

def two_sum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            # print(f"nums[{i}] + nums[{j}] = {nums[i] + nums[j]}")
            if (nums[i] + nums[j]) == target:
                return [i, j]
    return []
#%% Testing
print("\nExpected [1, 4], got :", two_sum([5, 1, 7, 2, 9, 3], 10))  
print("\nExpected [1, 3], got :", two_sum([4, 2, 11, 7, 6, 3], 9))  
print("\nExpected [0, 3], got :", two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print("\nExpected [1, 3], got :", two_sum([1, 3, 5, 7, 9], 10))  
print("\nExpected [], got :", two_sum([1, 2, 3, 4, 5], 10) )
print("\nExpected [2, 3], got :", two_sum([1, 2, 3, 4, 5], 7) )
print("\nExpected [0, 1], got :", two_sum([1, 2, 3, 4, 5], 3) )
print("\nExpected [], got :", two_sum([], 0) )
print("\nExpected [0,2], got :", two_sum([4, 5, 6], 10) )


#%%