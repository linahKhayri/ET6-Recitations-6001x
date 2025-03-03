"""
Created on Sun Mar  2 13:17:22 2025
@author: somai

Problem 2: Defensive Programming with Assertions

The function calculates the average of a list of numbers.
However, it **does not check** for an empty list, causing a ZeroDivisionError.

Your task:
1. Use **assertions** to prevent dividing by zero.
2. Modify the function to **handle an empty list safely**.
3. Ensure that invalid inputs (non-numeric values) are also **properly handled**.
"""

import builtins
def calculate_average(grades):
    """Returns the average of a list of grades."""
    return builtins.sum(grades) / len(grades)

# Test Cases
print(calculate_average([80, 90, 100]))  # Expected: 90.0
print(calculate_average([]))  # Expected: ERROR!

#Solution  


def calculate_average(grades):
    """Returns the average of a list of grades."""
    assert isinstance(grades, list), "Error: Your input must be a list."
    assert len(grades) > 0, "Error: Your list must not be empty."
    
    for grade in grades:
        assert isinstance(grade, (float, int)), "Error: Your input must be a number."
    
    return builtins.sum(grades) / len(grades)

# Test Cases with Exception Handling
try:
   print("Test 1:", calculate_average([80, 90, 100]))  # Expected: 90.0
   print("Test 2:", calculate_average([]))             # Expected: AssertionError (Empty list)
   print("Test 3:", calculate_average([80, "A", 100])) # Expected: AssertionError (Non-numeric value)
   print("Test 4:", calculate_average("not a list"))   #  Expected: AssertionError (Invalid input type)
   print("Test 5:", calculate_average({"grade": 90}))  #  Expected: AssertionError (Invalid input type - dictionary)
except AssertionError as e:
    print("Caught Error:", e)  #  Handle error properly
