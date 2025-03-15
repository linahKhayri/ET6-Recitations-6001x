"""
Created on Fri Mar 14 08:38:27 2025

@author: somai
"""
def mystery_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  #  Fix the function
    return arr

arr = [7, 2, 5, 1, 8]
print(mystery_sort(arr))  # Expected output: [1, 2, 5, 7, 8]
