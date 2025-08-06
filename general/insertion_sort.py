def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        The same list sorted in ascending order (in-place sorting)
    """
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be positioned
        j = i - 1     # Index of the last element in sorted portion
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at its correct position
        arr[j + 1] = key
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test the function
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    
    insertion_sort(test_array)
    print("Sorted array:", test_array)
    
    # Additional test cases
    print("\nAdditional examples:")
    
    # Empty array
    empty_array = []
    insertion_sort(empty_array)
    print("Empty array:", empty_array)
    
    # Single element
    single_element = [42]
    insertion_sort(single_element)
    print("Single element:", single_element)
    
    # Already sorted
    sorted_array = [1, 2, 3, 4, 5]
    insertion_sort(sorted_array)
    print("Already sorted:", sorted_array)
    
    # Reverse sorted
    reverse_array = [5, 4, 3, 2, 1]
    insertion_sort(reverse_array)
    print("Reverse sorted:", reverse_array)