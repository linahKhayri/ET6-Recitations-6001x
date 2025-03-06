##  Understanding the `intSet` Class: Custom Set Implementation

The `intSet` class is a **custom implementation** of a **set of integers** in Python. It allows inserting, removing, and checking membership of elements while ensuring **each integer appears only once** in the set.

---

## **1️⃣ The `intSet` Class Code**
```python
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'
```

---

## **🚀 Key Takeaways**
✔ **`intSet` mimics a mathematical set** but uses a Python list to store unique integers.  
✔ **Duplicate values are prevented** by checking before inserting.  
✔ `member()` **checks if an element exists in the set**.  
✔ `remove()` **deletes elements but raises an error if the element is missing**.  
✔ `__str__()` **provides a human-readable string representation** of the set.  

---

## **🔹 Two Important Tips**
### **1️⃣ `__str__` Method for Readable Output**
- The `__str__` method **formats an object as a human-readable string**.
- Helps when using `print(object)` instead of displaying memory addresses.
- Example:
  ```python
  def __str__(self):
      self.vals.sort()
      return '{' + ','.join(map(str, self.vals)) + '}'
  ```

### **2️⃣ Using `try-except` for Error Handling**
- **`try-except` prevents program crashes** when handling exceptions.
- Used in the `remove` method to catch missing elements:
  ```python
  def remove(self, e):
      try:
          self.vals.remove(e)
      except:
          raise ValueError(str(e) + ' not found')
  ```
- Instead of stopping execution, it **raises a controlled error message**.


