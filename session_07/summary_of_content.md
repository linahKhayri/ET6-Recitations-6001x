# Defensive Programming, Testing, and Debugging

## **1. Debugging Strategies (Lecture 7)**
### **Understanding Bugs**
- **Overt vs. Covert**: Visible crashes vs. incorrect but unnoticed results.
- **Persistent vs. Intermittent**: Always present vs. occasional errors.

### **Common Debugging Techniques**
- **Print Statements**: Use systematically to track variable changes.
- **Error Messages**: Learn common Python errors (IndexError, TypeError, etc.).
- **Binary Search Debugging**: Divide the code into sections and test step by step.
- **Explain Your Code**: Helps in identifying logical errors.
- **Use Assertions**: Validate assumptions in code.

## **2. Software Testing Approaches**

### **Black-Box Testing**
- Based on specifications, without seeing the code.
- Helps avoid developer bias.
- Useful for **boundary conditions** (empty lists, large/small numbers).

### **White-Box Testing (Glass-Box Testing)**
- Examines internal structure and execution paths.
- Ensures that all branches of the code are tested.
- More suitable for detecting **logical errors**.

## **3. Exception Handling & Error Management (Lecture 8)**

### **Types of Exceptions in Python**
- *SyntaxError, NameError, IndexError, TypeError, ValueError, IOError, ZeroDivisionError.*

### **Using Try-Except Blocks**
```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
```

### **`else` and `finally`**
- `else`: Executes when no errors occur.
- `finally`: Always executes, useful for **clean-up operations** (closing files, releasing resources).

## **4. Defensive Programming**
Defensive programming is a coding practice aimed at **reducing errors, improving maintainability, and ensuring robustness** by anticipating possible issues before they arise. It involves:

- **Writing clear specifications** for functions
  - Define expected inputs, outputs, and constraints.
- **Modularizing programs** for better readability and maintainability
  - Breaking complex logic into smaller, reusable functions.
- **Checking conditions on inputs and outputs (assertions)**
  - Use assertions and validations to catch unexpected values early.

## **5. Defensive Programming in Relation to Testing and Debugging**

### **Testing & Validation**
- Ensures that a program meets its specifications.
- **Compares input/output pairs** to expected results.
- Encourages the question: *“How can I break my program?”* to test edge cases.

### **Debugging**
- Identifies and fixes errors after they occur.
- **Studies events leading to errors**.
- Encourages the questions:
  - *“Why is it not working?”*
  - *“How can I fix my program?”*

## **6. Key Takeaways**
- **Defensive programming** prevents errors before they happen.
- **Testing & validation** detects errors by comparing behavior to expectations.
- **Debugging** fixes errors by analyzing their causes.

---

By following these practices, we can write **more reliable, maintainable, and error-resistant** code!
