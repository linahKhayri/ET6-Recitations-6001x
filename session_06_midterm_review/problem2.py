"""
10.0/10.0 points (graded)
Write a function called gcd that calculates the greatest common divisor of two positive integers. The gcd of two or more integers, when at least one of them is not zero, is the largest positive integer that divides the numbers without a remainder.

One way is recursively, where the greatest common denominator of a and b can be calculated as gcd(a, b) = gcd(b, a mod b). Hint: remember the mod symbol is % in Python. Do not import anything.

For example, the greatest common divisor (gcd) between a = 20 and b = 12 is:
gcd(20,12) is the same as gcd(12, 20 mod 12) = gcd(12,8)
gcd(12,8) is the same as gcd(8, 12 mod 8) = gcd(8,4)
gcd(8,4) is the same as gcd(4, 8 mod 4) = gcd(4,0)
The gcd is found (and the gcd is equal to a) when we reach 0 for b.

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    #YOUR CODE HERE
    """
#******************************************************************************************
"""
Created on Tue Feb 25 18:18:38 2025

@author: somai
Instructions:
1. Define a function `gcd(a, b)` that calculates the greatest common divisor (GCD) of two positive integers.
2. The function should return the largest positive integer that divides both `a` and `b` without leaving a remainder.
3. The greatest common divisor is calculated using the Euclidean algorithm, which is based on the following rule:
   gcd(a, b) = gcd(b, a % b)
   This means you replace `a` with `b`, and `b` with the remainder when `a` is divided by `b`.
   
4. The base case for this recursion occurs when `b` is 0. The reason for this is that:
   - The GCD of any number `a` and 0 is `a`. This is because every number divides 0, but `a` is the largest number that divides both `a` and 0.

Implementation Steps:
- If `b` is 0, return `a` as the GCD. This is the base case because if one of the numbers is 0, the other number is the GCD.
- Otherwise, recursively call the `gcd` function with `b` and `a % b` as arguments. The recursion continues until `b` becomes 0.

Example:
If a = 20 and b = 12:
- Step 1: gcd(20, 12) = gcd(12, 20 % 12) = gcd(12, 8)
- Step 2: gcd(12, 8) = gcd(8, 12 % 8) = gcd(8, 4)
- Step 3: gcd(8, 4) = gcd(4, 8 % 4) = gcd(4, 0)
- When `b` becomes 0, we return `a`, which is 4. Thus, the GCD of 20 and 12 is 4.
"""

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)  # Recursive call
