# Neeeds to find the max sum of 7 consecutive days
# Return an array that has the max 7 days sum
# and an array with with the first day in that 
# 7 day consecutive window, if more than one
# of thise consecutive sums exists, return
# all first days of these sums
# Example 1:
# Input:
# arr = [0, 2, 6, 4]
# Return: [None,[None]]
# Example 2:
# arr = [1, 2, 3, 4, 5, 6, 7]
# Return: [28,[1]]
# Example 3:
# arr = [1, 2, 3, 4, 5, 6, 7, 1]
# Return: [28,[1, 2]]

def max_7_day_sum(arr):
    # Check if we have at least 7 elements
    if len(arr) < 7:
        return [None, [None]]
    
    # Calculate sum of first window
    window_sum = sum(arr[:7])
    max_sum = window_sum
    max_positions = [1]  # 1-indexed
    
    # Slide the window
    for i in range(1, len(arr) - 6):
        # Update window sum by removing leftmost and adding rightmost
        window_sum = window_sum - arr[i-1] + arr[i+6]
        
        if window_sum > max_sum:
            max_sum = window_sum
            max_positions = [i + 1]  # 1-indexed
        elif window_sum == max_sum:
            max_positions.append(i + 1)  # 1-indexed
    
    return [max_sum, max_positions]

def run_tests():
    tests = [
        # Edge case: Empty array
        ([], [None, [None]], "Empty array"),
        
        # Edge case: Arrays with less than 7 elements
        ([1], [None, [None]], "Single element"),
        ([1, 2], [None, [None]], "Two elements"),
        ([1, 2, 3, 4, 5, 6], [None, [None]], "Six elements"),
        
        # Edge case: Exactly 7 elements
        ([1, 2, 3, 4, 5, 6, 7], [28, [1]], "Exactly 7 elements"),
        ([7, 6, 5, 4, 3, 2, 1], [28, [1]], "Exactly 7 elements descending"),
        
        # Edge case: 8 elements with two windows
        ([1, 2, 3, 4, 5, 6, 7, 1], [28, [1, 2]], "8 elements, tie at positions 1 and 2"),
        ([1, 2, 3, 4, 5, 6, 7, 8], [35, [2]], "8 elements, max at position 2"),
        
        # Edge case: All same numbers
        ([5, 5, 5, 5, 5, 5, 5, 5, 5], [35, [1, 2, 3]], "All same numbers"),
        ([0, 0, 0, 0, 0, 0, 0, 0], [0, [1, 2]], "All zeros"),
        
        # Edge case: Negative numbers
        ([-1, -2, -3, -4, -5, -6, -7], [-28, [1]], "All negative"),
        ([-1, -2, -3, -4, -5, -6, -7, -8], [-28, [1]], "All negative with 8 elements"),
        ([10, -5, 3, -2, 8, -1, 4, 2, -3], [17, [1]], "Mixed positive and negative"),
        
        # Edge case: Large positive and negative values
        ([100, 200, 300, 400, 500, 600, 700], [2800, [1]], "Large positive values"),
        ([-100, -200, -300, -400, -500, -600, -700], [-2800, [1]], "Large negative values"),
        
        # Edge case: Max sum at different positions
        ([1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 10], [70, [7]], "Max at end"),
        ([10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1], [70, [1]], "Max at beginning"),
        ([1, 1, 1, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1], [70, [4]], "Max in middle"),
        
        # Edge case: Multiple equal max sums non-consecutive
        ([5, 5, 5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 5, 5, 5], [35, [1, 10]], "Two equal max sums"),
        ([7, 1, 1, 1, 1, 1, 1, 0, 7, 1, 1, 1, 1, 1, 1], [13, [1, 9]], "Equal sums at edges"),
        
        # Edge case: Decreasing then increasing
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [49, [1, 13]], "Peak at start"),
        
        # Edge case: Zero sum window
        ([1, -1, 2, -2, 3, -3, 0, 5], [4, [2]], "Window sum equals zero"),
        
        # Edge case: Floating point numbers (if needed)
        ([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5], [31.5, [1]], "Floating point numbers"),
        
        # Original test cases
        ([0, 2, 6, 4], [None, [None]], "Original example 1"),
        ([1, 2, 3, 4, 5, 6, 7], [28, [1]], "Original example 2"),
        ([1, 2, 3, 4, 5, 6, 7, 1], [28, [1, 2]], "Original example 3"),
    ]
    
    passed = 0
    failed = 0
    
    for i, (input_arr, expected, description) in enumerate(tests, 1):
        result = max_7_day_sum(input_arr.copy())  # Use copy to avoid modification
        
        if result == expected:
            print(f"✓ Test {i:2d} PASSED: {description}")
            print(f"  Input: {input_arr}")
            print(f"  Output: {result}")
            passed += 1
        else:
            print(f"✗ Test {i:2d} FAILED: {description}")
            print(f"  Input: {input_arr}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
            failed += 1
        print()
    
    print(f"\n{'='*50}")
    print(f"Test Results: {passed} passed, {failed} failed out of {passed + failed} total")
    print(f"{'='*50}")

# Run all tests
if __name__ == "__main__":
    run_tests()
    
    arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    result1 = max_7_day_sum(arr1)
    print(f"All zeros: {arr1}")
    print(f"Result: {result1}")
    print(f"Explanation: All windows sum to 0, positions 1, 2, 3\n")
    
    # Case 2: All negative except zeros make max
    arr2 = [-5, -3, -2, -1, -4, -6, -7, 0, 0, 0, 0, 0, 0, 0]
    result2 = max_7_day_sum(arr2)
    print(f"Negatives with zeros at end: {arr2}")
    print(f"Result: {result2}")
    print(f"Explanation: Window at position 8 has sum 0 (all zeros), which is max\n")

    # Case 3: Mix that cancels to zero as best option
    arr3 = [1, -1, 2, -2, 3, -3, 0, -5, -10]
    result3 = max_7_day_sum(arr3)
    print(f"Mix canceling to zero: {arr3}")
    print(f"Result: {result3}")
    print(f"Explanation: First window sums to 0, better than negative sums\n")

    # Case 4: Multiple windows with zero sum
    arr4 = [1, -1, 1, -1, 1, -1, 0, 0, 2, -2, 2, -2, 2, -2]
    result4 = max_7_day_sum(arr4)
    print(f"Multiple zero-sum windows: {arr4}")
    print(f"Result: {result4}")
    print(f"Explanation: Multiple windows achieve max sum of 0\n")

    # Case 5: All negative numbers
    arr5 = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    result5 = max_7_day_sum(arr5)
    print(f"All negative: {arr5}")
    print(f"Result: {result5}")
    print(f"Explanation: Best window has negative sum, not zero\n")