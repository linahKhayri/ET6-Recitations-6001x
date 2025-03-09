## **Understanding Object-Oriented Programming (OOP) Through the GradeBook Example**

### **Overview**
This example demonstrates key **Object-Oriented Programming (OOP) principles** including:
- **Encapsulation** → Managing student data and grades within dedicated classes.
- **Inheritance** → Reusing and extending functionality from parent classes.
- **Method Overriding** → Customizing behaviors in subclasses.
- **Separation of Concerns (SoC)** → Ensuring different responsibilities are assigned to specific classes.

---

## **1️⃣ Encapsulation: Organizing Data & Behavior**
Encapsulation ensures that **data and related behaviors** are contained within relevant classes.

### **🔹 Example: `Person` Class (Encapsulates Identity)**
```python
import datetime
class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        return self.lastName

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        if self.birthday is None:
            raise ValueError("Birthday not set")
        return (datetime.date.today() - self.birthday).days

    def __str__(self):
        return self.name
```
✅ **Encapsulation Ensures:**
- Attributes (`name`, `birthday`, `lastName`) belong to `Person`.
- Methods (`getLastName()`, `getAge()`) operate on the same object.
- Changes in `Person` do not affect unrelated classes.

---

## **2️⃣ Inheritance: Reusing and Extending Behavior**
Inheritance allows **a new class to derive properties and behaviors from an existing class**.

### **🔹 Example: `MITPerson` Inherits from `Person`**
```python
class MITPerson(Person):
    nextIdNum = 0  # Class attribute for unique IDs
    
    def __init__(self, name):
        super().__init__(name)  # Calls Person's constructor
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum
```
✅ **Why Use Inheritance?**
- `MITPerson` **inherits** `Person`'s identity attributes (`name`, `birthday`).
- `MITPerson` **adds new functionality** (`idNum` for university ID).
- **Code reuse** → No need to rewrite name and birthday handling.

---

## **3️⃣ Method Overriding: Customizing Behavior in Subclasses**
Method overriding allows **subclasses to modify inherited methods** to provide specialized behavior.

### **🔹 Example: Overriding `__lt__()` in `MITPerson`**
```python
    def __lt__(self, other):
        return self.idNum < other.idNum  # Overridden: Now sorts by ID instead of last name
```
✅ **Key Benefits of Overriding:**
- `Person` sorted by last name, but `MITPerson` sorts by **ID number**.
- Subclasses **modify inherited methods without changing parent behavior**.

---

## **4️⃣ Separation of Concerns (SoC): Organizing Responsibilities**
SoC ensures that each **class has a clear, distinct responsibility**.

### **🔹 Example: `Grades` Class Manages Grades Separately**
```python
class Grades(object):
    def __init__(self):
        self.students = []  # List of student objects
        self.grades = {}  # Dictionary mapping students to grades
        self.isSorted = True  # Optimization flag for sorting

    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        try:
            self.grades[student].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        try:
            return self.grades[student][:]
        except KeyError:
            raise ValueError('Student not in grade book')
```
✅ **Why Use SoC?**
- `Person`, `MITPerson`, `UG`, and `Grad` focus on identity.
- `Grades` **manages academic records separately**, avoiding code clutter.
- Changes to grade storage **do not impact student identity**.

---

## **5️⃣ Generators (`yield`): Efficient Iteration**
Instead of returning a full list, generators allow **on-demand data retrieval**.

### **🔹 Example: `getGrades()` Uses `yield`**
```python
def getGrades(self, student):
    for grade in self.grades[student]:
        yield grade  # Instead of returning all at once, yield values one-by-one
```
✅ **Why Use `yield`?**
- **Reduces memory usage** (especially useful for large datasets).
- **Supports lazy evaluation**, retrieving values only when needed.

---

## **Key Takeaways: OOP Principles in Action**
✅ **Encapsulation** → Keeps related data and behaviors together.  
✅ **Inheritance** → Promotes **code reuse and specialization**.  
✅ **Method Overriding** → Allows **subclasses to modify behaviors**.  
✅ **Separation of Concerns** → Organizes responsibilities into **distinct, maintainable classes**.  
✅ **Generators (`yield`)** → Optimize data retrieval for **better performance**.  

---

