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
