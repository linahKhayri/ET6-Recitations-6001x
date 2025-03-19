##  Understanding the `fraction` Class: Special Methods, `self` & `other`, and Math Concepts

The `fraction` class demonstrates **object-oriented programming (OOP)** principles, implementing mathematical operations using **special methods (dunder methods)**. Let’s analyze it step by step.

---

## **1️⃣ The `fraction` Class Code**
```python
class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)
    
    def getNumer(self):
        return self.numer
    
    def getDenom(self):
        return self.denom
    
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                   + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                   - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    
    def convert(self):
        return self.getNumer() / self.getDenom()
```

---

## **2️⃣ Built-in Special Methods in Python**
Python provides **special methods** (also called **dunder methods**, short for *double underscore methods*) that allow objects to interact with built-in operators and functions.

### **🔹 `__add__` Method (`+` Operator Overloading)**
```python
def __add__(self, other):
    numerNew = other.getDenom() * self.getNumer() \
               + other.getNumer() * self.getDenom()
    denomNew = other.getDenom() * self.getDenom()
    return fraction(numerNew, denomNew)
```
#### **What does `__add__` do?**
- It **overrides the `+` operator** so that when two `fraction` objects are added (`f1 + f2`), Python internally calls:
  ```python
  f1.__add__(f2)
  ```
- The function **computes a new fraction**, using the formula for fraction addition:

  $$
  \frac{a}{b} + \frac{c}{d} = \frac{a \times d + c \times b}{b \times d}
  $$

---

### **🔹 `__sub__` Method (`-` Operator Overloading)**
```python
def __sub__(self, other):
    numerNew = other.getDenom() * self.getNumer() \
               - other.getNumer() * self.getDenom()
    denomNew = other.getDenom() * self.getDenom()
    return fraction(numerNew, denomNew)
```
#### **What does `__sub__` do?**
- Similar to `__add__`, this **overrides the `-` operator** so that `f1 - f2` calls:
  ```python
  f1.__sub__(f2)
  ```
- Computes fraction subtraction using:
  
  ```math
  \frac{a}{b} - \frac{c}{d} = \frac{a \times d - c \times b}{b \times d}


---

## **3️⃣ Understanding `self` and `other`**
### **🔹 What is `self`?**
- `self` refers to the **current instance** of the class.
- It allows methods to **access attributes (`self.numer`, `self.denom`) and other methods (`self.getNumer()`)**.

### **🔹 What is `other`?**
- `other` represents **the second object** in operations like `+` and `-`.
- When `f1 + f2` is written:
  - `self` → refers to `f1`
  - `other` → refers to `f2`

---

## **4️⃣ Mathematical Concepts Behind the Code**
The class models **basic fraction arithmetic**, specifically **addition, subtraction, and conversion to decimal**.

### **🔹 Fraction Addition Formula**
$$
\frac{a}{b} + \frac{c}{d} = \frac{a \times d + c \times b}{b \times d}
$$

### **🔹 Fraction Subtraction Formula**
$$
\frac{a}{b} - \frac{c}{d} = \frac{a \times d - c \times b}{b \times d}
$$

### **🔹 Fraction to Decimal Conversion**
```python
def convert(self):
    return self.getNumer() / self.getDenom()
```

---

## **5️⃣ Final Example: Running the Code**
```python
f1 = fraction(3, 4)
f2 = fraction(5, 6)

print(f1)  # Output: "3 / 4"
print(f2)  # Output: "5 / 6"

f3 = f1 + f2
print(f3)  # Output: "38 / 24"

f4 = f1 - f2
print(f4)  # Output: "-2 / 24"

print(f1.convert())  # Output: 0.75
print(f2.convert())  # Output: 0.8333333333333334
```

---

## **Conclusion**
 ✔ **Python’s special methods (`__add__`, `__sub__`, `__str__`) enable operator overloading.**  
 ✔ **`self` refers to the current object, while `other` is the second operand in operations like `+` and `-`.**  
✔ **Fraction addition & subtraction require denominator alignment using cross multiplication.**  
✔ **The class converts fractions to decimal format using `convert()`.**  




