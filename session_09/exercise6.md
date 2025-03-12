# **Comparison of Complexity**

## **Overview**
This document compares four different functions in terms of **time complexity** and provides a brief explanation of each.

| Function | Time Complexity | Explanation |
|----------|---------------|-------------|
| **First Code (while loop, `n *= 2`)** | \( O(1) \) | Runs a **fixed number of iterations (5)**, so the complexity is constant regardless of `n`. |
| **`iterPower(a, b)` (Iterative Exponentiation)** | \( O(b) \) | Uses a loop that runs **\( b \) times**, multiplying `result` by `a` in each step. |
| **`recurPower(a, b)` (Recursive Exponentiation)** | \( O(b) \) | Calls itself recursively **\( b \) times**, multiplying `a` at each step. |
| **`recurPowerNew(a, b)` (Exponentiation by Squaring)** | \( O(\log b) \) | **Efficient approach**, reducing `b` by **half** each step when `b` is even, significantly improving performance. |

---

## **Brief Explanation of Each Code**

### **1️⃣ First Code (`while i < 5`)**
```python
# Assume n has been previously bound to some value 
i = 0
while i < 5:
   n *= 2
   i += 1

print(n)
```
- **Complexity: \( O(1) \)**
- **Explanation:** The loop **always runs exactly 5 times**, regardless of the value of `n`. Since the number of operations is **constant**, the time complexity is **\( O(1) \)**.

---

### **2️⃣ `iterPower(a, b)` (Iterative Exponentiation)**
```python
def iterPower(a, b):
   result = 1
   while b > 0:
      result *= a
      b -= 1
   return result
```
- **Complexity: \( O(b) \)**
- **Explanation:** This function uses a `while` loop that **runs \( b \) times**, multiplying `result` by `a` in each step. The time complexity is **\( O(b) \) (linear time)**.

---

### **3️⃣ `recurPower(a, b)` (Recursive Exponentiation)**
```python
def recurPower(a, b):
   print(a, b)
   if b == 0:
      return 1
   else:
      return a * recurPower(a, b-1)
```
- **Complexity: \( O(b) \)**
- **Explanation:** This function **recursively calls itself \( b \) times**, reducing `b` by `1` in each step. Since the function performs **one multiplication per call**, the total number of operations is **proportional to \( b \)**.

---

### **4️⃣ `recurPowerNew(a, b)` (Exponentiation by Squaring)**
```python
def recurPowerNew(a, b):
   print(a, b)
   if b == 0:
      return 1
   elif b % 2 == 0:
      return recurPowerNew(a * a, b // 2)
   else:
      return a * recurPowerNew(a, b - 1)
```
- **Complexity: \( O(\log b) \)**
- **Explanation:**  
  - When `b` is **even**, the function **squares `a` and halves `b`**, reducing `b` much faster.
  - When `b` is **odd**, it follows the standard recursive exponentiation approach (`a * recurPowerNew(a, b-1)`).
  - Since the function **halves `b` when possible**, the number of recursive calls is **logarithmic**, making it **much faster** than `iterPower` or `recurPower`.

---

## **Conclusion**
1. **First code is the fastest \( O(1) \) because it runs a fixed number of times.**  
2. **Both `iterPower` and `recurPower` are slow \( O(b) \) because they execute `b` multiplications.**  
3. **`recurPowerNew` (Exponentiation by Squaring) is the most efficient \( O(\log b) \), reducing the number of steps significantly.**  

**Use `recurPowerNew` for large exponents to improve performance!** 
