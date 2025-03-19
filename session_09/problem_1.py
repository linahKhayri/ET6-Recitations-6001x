"""
Created on Fri Mar 14 08:38:27 2025

@author: somai
"""
def mystery_sort(arr):
    """
    This function implements Selection Sort.
    Complexity: O(n^2)
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
    if min_index !=i: #Added condition to improve efficiency
        arr[i], arr[min_index] = arr[min_index], arr[i]  
    return arr

arr = [7, 2, 5, 1, 8]
print(mystery_sort(arr))  # Expected output: [1, 2, 5, 7, 8]
"""
Correctness: Sorting logic is correct.
Optimization:  Check min_index != i before swapping to reduce redundant swaps.
Complexity:  Best, worst, and average cases remain O(n²).
"""
