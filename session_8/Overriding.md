## UML Class Diagram: Method Overriding & Attribute Overriding in Python

### **Overview**
This UML class diagram represents a multiple inheritance structure where class `D` inherits from both `C` and `B`, while `B` inherits from `A`. Understanding how Python resolves **method overriding** and **attribute overriding** in such cases is crucial.

### **Class Diagram**
<p align="center">
  <img src="https://raw.githubusercontent.com/MIT-Emerging-Talent/ET6-Recitations-6001x/main/session_8/UML%20class.png" width="500">
</p>

### **Python Code Representation**
```python
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

# Example Execution
obj = D()
print(obj.a)  # Output: 2 (Overwritten by B.__init__())  # Attribute Resolution
print(obj.b)  # Output: 3 (From B.__init__())
print(obj.c)  # Output: 5 (From C.__init__())
print(obj.d)  # Output: 6 (From D.__init__())
obj.x()  # Output: A.x (Found in class A via MRO)  # Method Resolution
obj.y()  # Output: C.y (First match in MRO: D → C → B → A)
obj.z()  # Output: D.z (Method overridden in D)
```

### **🔹 Important Tips**
1️⃣ **Method Resolution Order (MRO):** Python determines method calls based on MRO. Use `print(D.mro())` to check the order.

2️⃣ **Constructor Execution:** Python **does not automatically call constructors** in multiple inheritance. Explicit calls like `C.__init__(self)` and `B.__init__(self)` are required.

3️⃣ **Attribute Overriding:** `D` inherits `a` from both `C` and `B`, but **the last constructor called (`B.__init__()`) decides the final value of `a`**.

4️⃣ **Method Overriding:** `D` overrides `z()`, meaning `obj.z()` will always call `D.z()` instead of `C.z()` or `B.z()`.

5️⃣ **Use `super()` for Better Control:** Instead of `C.__init__(self)` and `B.__init__(self)`, using `super().__init__()` ensures constructors follow MRO automatically.


