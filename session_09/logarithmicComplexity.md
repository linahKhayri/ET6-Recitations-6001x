# **Understanding Logarithmic Complexity (O(log n))**

Logarithmic complexity describes algorithms where **the number of steps grows as the logarithm of the input size**. This means that instead of processing **every** element like in \( O(n) \), an \( O(log n) \) algorithm **reduces the problem size significantly at each step**—usually by dividing it by a constant factor (such as 2).  

## **What Does "Logarithm" Mean in Complexity?**
A **logarithm** is the inverse of exponentiation. The logarithm **\( log_b(n) \)** answers the question:  
**"To what power must \( b \) be raised to get \( n \)?"**  

### **Mathematically:**
$$
\log_b(n) = x \quad \text{if and only if} \quad b^x = n
$$

Where:
- \( b \) is the **base** (often 2 in computer science).
- \( n \) is the **input size**.
- \( x \) is the **number of times you must divide \( n \) by \( b \) to reach 1**.

### **Example: Logarithm in Base 2**
$$
log_2(8) = 3 \quad \text{because} \quad 2^3 = 8
$$
$$
log_2(16) = 4 \quad \text{because} \quad 2^4 = 16
$$
$$
\log_2(1024) = 10 \quad \text{because} \quad 2^{10} = 1024
$$

This tells us that if an algorithm **cuts the problem size in half** each step, it will finish in about \( \log_2(n) \) steps.

---

## **How Logarithmic Complexity Appears in Algorithms**
### **Example: Binary Search**
One of the most famous \( O(log n) \) algorithms is **binary search**, which finds an element in a sorted list by repeatedly halving the search space.

### **How It Works**:
1. Look at the **middle** element of the sorted list.
2. If it's the target, return it.
3. If the target is smaller, search only in the **left half**.
4. If the target is larger, search only in the **right half**.
5. Repeat until the element is found or the list is empty.

### **Log Calculation for Steps**:
- A list of **size 8** requires at most **$\log_2(8)$ = 3 steps**.
- A list of **size 16** requires at most **$\log_2(16)$ = 4 steps**.
- A list of **size 1,000,000** requires only **$\log_2(1,000,000) \approx 20$ steps**.


#### **Python Implementation**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Find middle index
        if arr[mid] == target:
            return mid  # Found target
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    return -1  # Target not found
```
 **Binary search runs in \( O(log n) \) time.**

---

## **Log Growth vs. Other Complexities**
| \( n \) (Input Size) | $\log_2(n)$ (Steps in \( O(log n) \)) | \( O(n) \) (Linear Steps) |
|----------------|----------------------|-------------------|
| 8  | 3  | 8  |
| 16 | 4  | 16 |
| 32 | 5  | 32 |
| 1024 | 10 | 1024 |
| 1,000,000 | 20 | 1,000,000 |

### **Key Takeaway**:  
Logarithmic complexity grows **much slower** than linear complexity. Even for **1 million elements**, we only need **about 20 steps** in \( O(log n) \) vs. **1 million steps** in \( O(n) \).

---

## **Conclusion**
1. **Logarithmic complexity (\( O(log n) \)) means that the number of steps grows as the log of the input size**.
2. **It appears when an algorithm repeatedly halves or divides the input size** (e.g., Binary Search, tree-based operations).
3. **Logarithmic growth is very slow**, making \( O(log n) \) algorithms **extremely efficient** compared to \( O(n) \) or \( O(n^2) \).

 **If an algorithm halves the problem each time, its complexity is \( O(log n) \).** 
