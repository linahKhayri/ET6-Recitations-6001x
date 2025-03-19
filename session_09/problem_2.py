"""
Created on Fri Mar 14 08:38:27 2025

@author: somai
"""
def sort_A(arr): # Bubble Sort O(n^2)
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sort_B(arr): # Merge Sort O(n log n)
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sort_B(arr[:mid])
    right = sort_B(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """ Implements merge step of Merge Sort """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    pass

def sort_C(arr): #  Selection Sort O(n^2)
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
