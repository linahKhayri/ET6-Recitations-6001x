## UML Class Diagram: Method Overriding & Attribute Overriding in Python

### **Overview**
This UML class diagram represents a multiple inheritance structure where class `D` inherits from both `C` and `B`, while `B` inherits from `A`. Understanding how Python resolves **method overriding** and **attribute overriding** in such cases is crucial.

### **Class Diagram**
![UML Class Diagram](sandbox:/mnt/data/UML%20class_corrected.png)

### **Python Code Representation**
```python
class A:
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

class C:
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):  # Multiple Inheritance
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

# Example Execution
obj = D()
print(obj.a)  # Attribute Resolution
print(obj.b)
print(obj.c)
print(obj.d)
obj.x()  # Method Resolution
obj.y()
obj.z()
```

### **🔹 Important Tips**
1️⃣ **Method Resolution Order (MRO):** Python determines method calls based on MRO. Use `print(D.mro())` to check the order.

2️⃣ **Constructor Execution:** Python **does not automatically call constructors** in multiple inheritance. Explicit calls like `C.__init__(self)` and `B.__init__(self)` are required.

3️⃣ **Attribute Overriding:** `D` inherits `a` from both `C` and `B`, but **the last constructor called (`B.__init__()`) decides the final value of `a`**.

4️⃣ **Method Overriding:** `D` overrides `z()`, meaning `obj.z()` will always call `D.z()` instead of `C.z()` or `B.z()`.

5️⃣ **Use `super()` for Better Control:** Instead of `C.__init__(self)` and `B.__init__(self)`, using `super().__init__()` ensures constructors follow MRO automatically.

---

This Markdown file provides a **concise guide** to understanding **method overriding and attribute overriding in Python** using UML representation. 🚀
