# **Solutions: Interactive Coding Exercises**

🔗 **Reference for Sorting Algorithms:** [VisuAlgo Sorting](https://visualgo.net/en/sorting?slide=1)

## **🔹 Solution 1: Debugging & Analyzing Sorting Algorithms**

### **Task 1: Identify the Sorting Algorithm**
Below is the fixed sorting function. This represents **Selection Sort**.

```python
def mystery_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # ✅ Swap elements to complete the sort
    return arr

arr = [7, 2, 5, 1, 8]
print(mystery_sort(arr))  # Output: [1, 2, 5, 7, 8]
```
### **Answers:**
1. **Sorting Algorithm:** Selection Sort.
2. **What is the Big-O notation for the best, worst, and average cases?**
   - **Best Case:** O(n²) (Even if the list is sorted, it still checks all elements).
   - **Worst Case:** O(n²) (Reverse order requires maximum swaps).
   - **Average Case:** O(n²).

---

## **🔹 Solution 2: Understanding Time Complexity**

### **Task 2: Compare Sorting Algorithm Complexities**
Below are the corrected sorting functions with their corresponding algorithms.

```python
def sort_A(arr):  # ✅ Bubble Sort (O(n²))
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sort_B(arr):  # ✅ Merge Sort (O(n log n))
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sort_B(arr[:mid])
    right = sort_B(arr[mid:])
    return merge(left, right)

def merge(left, right):
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

def sort_C(arr):  # ✅ Selection Sort (O(n²))
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```
### **Answers:**
| Function | Sorting Algorithm | Best Case | Worst Case | Average Case |
|----------|------------------|-----------|------------|--------------|
| `sort_A` | Bubble Sort | O(n) | O(n²) | O(n²) |
| `sort_B` | Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| `sort_C` | Selection Sort | O(n²) | O(n²) | O(n²) |

---

## **🔹 Solution 3: Writing an Optimized Sorting Algorithm**

### **Task 3: Implement an Optimized Bubble Sort**
Bubble Sort can be optimized by stopping early if no swaps occur.

```python
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # ✅ Optimization: Stop if the list is already sorted
    return arr

arr = [4, 2, 7, 1, 9]
print(optimized_bubble_sort(arr))  # Output: [1, 2, 4, 7, 9]
```
### **Answers:**
1. **Why is this version better?**
   - Reduces unnecessary comparisons.
   - Stops early if no swaps occur (Best case O(n)).

2. **What is the Big-O notation for best, worst, and average cases?**
   - **Best Case:** O(n) (Already sorted, only one pass).
   - **Worst Case:** O(n²) (Reverse sorted list, full iterations needed).
   - **Average Case:** O(n²).

---

### **Summary of Solutions:**
✅ Selection Sort debugged and analyzed with Big-O notation.
✅ Complexity analysis of sorting functions, comparing best, worst, and average cases.
✅ Optimized Bubble Sort implementation with complexity breakdown.

These solutions serve as a reference while students work through the exercises! 
