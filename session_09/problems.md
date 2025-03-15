# **Interactive Coding Exercises for Students**

🔗 **Step 1: Explore Sorting Algorithms** *(Estimated Time: 15 minutes)*
Before working on the exercises, go through the [VisuAlgo Sorting](https://visualgo.net/en/sorting?slide=1) link and:
1. Explore the **Bubble Sort, Selection Sort, and Merge Sort** animations.
2. Analyze their **pseudocode** and compare their working mechanisms.
3. Test different lists and observe how the sorting behavior changes.

---

## **🔹 Exercise 1: Debugging & Analyzing Sorting Algorithms** *(Estimated Time: 15 minutes)*

### **Task 1: Identify the Sorting Algorithm**
Below is an incomplete sorting function. Identify which sorting algorithm it represents and fix the missing parts.

```python
def mystery_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Fix: Swap elements to complete the sort
    return arr

arr = [7, 2, 5, 1, 8]
print(mystery_sort(arr))  # Expected output: [1, 2, 5, 7, 8]
```
🔹 **Questions:**
1. What sorting algorithm is being implemented?
2. What is its worst-case complexity?

---

## **🔹 Exercise 2: Understanding Time Complexity** *(Estimated Time: 15 minutes)*
### **Task 2: Compare Sorting Algorithm Complexities**
The following sorting functions have different time complexities. Your task is to analyze them and determine their efficiency.

```python
def sort_A(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sort_B(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sort_B(arr[:mid])
    right = sort_B(arr[mid:])
    return merge(left, right)

# Complete the merge function!

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

def sort_C(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```
🔹 **Questions:**
1. Identify which sorting algorithm each function represents.
2. Determine their best-case, average-case, and worst-case time complexity.

---

## **🔹 Exercise 3: Writing an Optimized Sorting Algorithm** *(Estimated Time: 15 minutes)*
### **Task 3: Implement an Optimized Bubble Sort**
Bubble Sort is inefficient in its basic form. Modify the code below to:
1. Reduce unnecessary comparisons.
2. Stop early if no swaps occur.

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
            break  # Optimization: Stop if the list is already sorted
    return arr

arr = [4, 2, 7, 1, 9]
print(optimized_bubble_sort(arr))  # Expected: [1, 2, 4, 7, 9]
```
🔹 **Questions:**
1. Why does this version perform better than the standard Bubble Sort?
2. What is the best-case time complexity of the optimized version?

---

These exercises will help you understand sorting algorithms at a deeper level! 
