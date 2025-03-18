"""
Created on Fri Mar 14 08:38:27 2025

@author: somai
"""
def optimized_bubble_sort(arr):
    """
    Optimized Bubble Sort
    - Best Case: O(n) when already sorted
    - Worst & Average Case: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  #  Stops early if no swaps occur
    return arr

arr = [4, 2, 7, 1, 9]
print(optimized_bubble_sort(arr))  # Expected output: [1, 2, 4, 7, 9]


