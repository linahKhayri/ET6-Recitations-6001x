# **Recitation Review: Sorting, Searching, Recursion & Complexity**

## **1️⃣ Concept Review**

### **🔹 Recursion Complexity (`O(n)`, `O(log n)`)**
- **Recursive functions** call themselves, reducing problem size in each step.
- If recursion **reduces `n` by 1 each time**, complexity is **O(n)**.
- If recursion **halves `n` each time**, complexity is **O(log n)**.

### **🔹 Sorting Algorithms**
#### **Bubble Sort (O(n²))**
- Compares and swaps adjacent elements.
- Slowly moves largest values to the end.

#### **Selection Sort (O(n²))**
- Finds the smallest element and places it in the correct position.
- Repeats for each index.

#### **Merge Sort (O(n log n))**
- Uses **divide & conquer** to split and merge sorted sublists.
- Efficient for large datasets.

### **🔹 Searching Algorithms**
#### **Linear Search (O(n))**
- Checks each element one by one.
- Works for unsorted lists.

#### **Binary Search (O(log n))**
- Works **only for sorted lists**.
- Repeatedly halves the search space.

### **🔹 Complexity Comparisons**
| Algorithm | Best Case | Worst Case | Explanation |
|-----------|----------|------------|-------------|
| **Bubble Sort** | O(n) | O(n²) | Slow for large lists |
| **Selection Sort** | O(n²) | O(n²) | Always scans full list |
| **Merge Sort** | O(n log n) | O(n log n) | Efficient for large data |
| **Linear Search** | O(1) | O(n) | Scans the whole list in worst case |
| **Binary Search** | O(1) | O(log n) | Fast, but only for sorted lists |

---

## **2️⃣ Recap & Takeaways**
- **Recursion Complexity:** `O(n)` when reducing `n-1`, `O(log n)` when halving.
- **Merge Sort is `O(n log n)`**, more efficient than Bubble/Selection Sort.
- **Binary Search is `O(log n)`, faster than Linear Search (`O(n)`).**
- **Sorting is critical for efficient searching!**

---

## **3️⃣ Algorithm Complexity Growth Visualization**

This chart illustrates the growth of different complexities (O(1), O(log n), O(n), O(n log n), O(n²), etc.).

<p align="center">
  <img src="https://raw.githubusercontent.com/MIT-Emerging-Talent/ET6-Recitations-6001x/main/session_09/complx.png" width="600">
</p>

---
    
 **Next Steps:** Try modifying the exercises, changing input sizes, and analyzing performance!

