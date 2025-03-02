# **Debugging and Defensive Programming Problems**

This document contains a set of problems designed for **recitation sessions** focused on **debugging, exception handling, and defensive programming**. Each problem includes **instructions, explanations, and sample test cases** to guide learners through solving them.

---

## **Problem 1: Debugging a Function with Logical Errors**
### **Objective**
- Identify and fix **logical errors** in a function that checks whether a number is prime.

### **Instructions**
1. Run the given code and identify incorrect outputs.
2. Debug the function using **print statements** and logical reasoning.
3. Optimize the function for better performance.
4. Test with different cases, including edge cases.

### **Buggy Code**
```python
import math

def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n == 1:
        return True  # Incorrect logic
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

### **Test Cases**
```python
print(is_prime(1))   # Expected: False
print(is_prime(2))   # Expected: True
print(is_prime(9))   # Expected: False
print(is_prime(11))  # Expected: True
print(is_prime(17))  # Expected: True
print(is_prime(25))  # Expected: False
```

### **Expected Issues**
- The function incorrectly assumes `1` is prime.
- Inefficient loop; it should iterate only up to `sqrt(n) + 1`.

### **Solution**
```python
import math

def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```

---

## **Problem 2: Exception Handling in User Input**
### **Objective**
- Prevent program crashes caused by **invalid input** and **division by zero**.

### **Instructions**
1. Run the code and observe what happens when entering non-numeric values or `0`.
2. Use `try-except` to handle **ValueError** and **ZeroDivisionError**.
3. Ensure the program keeps prompting until valid input is received.

### **Buggy Code**
```python
def divide_numbers():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    result = int(num1) / int(num2)
    print(f"Result: {result}")

divide_numbers()
```

### **Solution**
```python
def divide_numbers():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 / num2
            print(f"Result: {result}")
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")
        except ZeroDivisionError:
            print("Cannot divide by zero! Please enter a nonzero denominator.")

divide_numbers()
```

---

## **Problem 3: Defensive Programming with Assertions**
### **Objective**
- Use **assertions** to catch invalid cases before execution proceeds.

### **Instructions**
1. Run the function with an **empty list** to see what happens.
2. Modify the function to include **assertions**.
3. Ensure meaningful error messages are displayed when assertions fail.

### **Buggy Code**
```python
def calculate_average(grades):
    return sum(grades) / len(grades)
```

### **Solution**
```python
def calculate_average(grades):
    """Returns the average of a list of grades."""
    assert len(grades) > 0, "Error: List of grades cannot be empty!"
    return sum(grades) / len(grades)
```

---

## **Problem 4: Black-Box Testing for a Square Root Function**
### **Objective**
- Identify edge cases and modify a function to handle them correctly.

### **Instructions**
1. Run the function with **negative numbers**.
2. Apply **black-box testing** to explore different inputs.
3. Modify the function to raise an exception for invalid inputs.

### **Buggy Code**
```python
def sqrt(x, eps=0.0001):
    low, high = 0, x
    guess = (low + high) / 2
    while abs(guess**2 - x) > eps:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess
```

### **Solution**
```python
def sqrt(x, eps=0.0001):
    """Returns the approximate square root of x using binary search."""
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    if x == 0:
        return 0
    
    low, high = 0, x
    guess = (low + high) / 2
    while abs(guess**2 - x) > eps:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess
```

---

## **Problem 5: Handling Missing Dictionary Keys**
### **Objective**
- Handle missing keys in a dictionary gracefully.

### **Instructions**
1. Modify the function to return a **default value** when a key is missing.
2. Use **dictionary methods** to improve robustness.

### **Buggy Code**
```python
prices = {"apple": 1.5, "banana": 0.75, "orange": 1.0}

def get_price(item):
    return prices[item]  # KeyError if item is not in the dictionary
```

### **Solution**
```python
def get_price(item):
    """Returns the price of an item, or a default value if not found."""
    return prices.get(item, "Item not found")
```

---

## **Final Notes**
- These problems are designed to **enhance debugging, testing, and defensive coding skills**.
- Encourage students to **think critically and apply debugging systematically**.
- Solutions are provided for reference but encourage independent problem-solving first.

Would you like any refinements or additional challenges? 🚀
