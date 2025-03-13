# **Comparison of Complexity for Given Search Functions**

## **Brief Explanation of Each Code**

### **1️⃣ `search(L, e)` (Linear Search on Sorted List - Inefficient)**
```python
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```
- **Complexity: \( O(n) \)**
- **Explanation:**
  - The function iterates over the list until it either finds `e` or encounters a value greater than `e`.
  - **Best case:** If `e` is near the start, the function returns early.
  - **Worst case:** If `e` is not present, the function iterates through the entire list.
  - **Overall, the complexity remains \( O(n) \), where \( n \) is `len(L)`.**

---

### **2️⃣ `bisect_search1(L, e)` (Binary Search with Slicing - Inefficient)**
```python
def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search1(L[:half], e)  # Creates a new list (slicing + copying)
        else:
            return bisect_search1(L[half:], e)  # Creates a new list (slicing + copying)
```
- **Complexity:** $O (n log n)$
- **Explanation:**
  - This function **halves the search space** at each step (which suggests $O(log n) $).
  - However, **it slices the list (`L[:half]`, `L[half:]`) at each step**, which requires copying part of the list, leading to an **extra cost that sums to \( O(n) \) overall**.
  - **Total complexity: $O(n log n) $ because of both slicing and recursive calls.**
  - ✅ **Important Note:** Slicing (`L[:half]`, `L[half:]`) creates a new list, making `bisect_search1` inefficient compared to using index-based binary search.

---

### **3️⃣ `bisect_search2(L, e)` (Optimized Binary Search with Indices - Efficient)**
```python
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
```
- **Complexity: $O(log n) $**
- **Explanation:**
  - Uses **indexing (`low` and `high`) instead of slicing**, eliminating unnecessary list copying.
  - **Halves the search space** at each step while keeping track of the search range.
  - Achieves the **optimal binary search complexity of $O(log n) $**.

---

## **Final Comparison Table**
| Function | Time Complexity | Explanation |
|----------|---------------|-------------|
| **`search(L, e)` (Linear Search on Sorted List)** | \( O(n) \) | Iterates through the list, stopping early if `e` is found or a greater element is encountered. |
| **`bisect_search1(L, e)` (Binary Search with Slicing)** | $O(n log n) $ | **Inefficient due to slicing**, which copies part of the list at each recursive call, increasing complexity. |
| **`bisect_search2(L, e)` (Optimized Binary Search with Indices)** | $O(log n) $ | **Efficient binary search**, avoiding slicing by using indices to track the search space, achieving the optimal logarithmic complexity. |

 **Use `bisect_search2` for efficient searches!** 
