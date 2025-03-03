"""
Created on Sun Mar  2 13:17:22 2025
@author: somai

Problem 1: Handling User Input with Exceptions
Objective:
Prevent program crashes caused by invalid input and division by zero.

The function below takes two numbers as input and divides them.
However, the program crashes if:
- The user enters a non-numeric value.
- The user tries to divide by zero.

Your task:
1. Identify the **potential runtime errors**.
2. Modify the function to **handle exceptions gracefully**.
3. Ensure the program **keeps asking for valid input** if an error occurs.
"""

def divide_numbers():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    result = int(num1) / int(num2)
    print("Result:", result)

divide_numbers()

#Robust Version
def divide_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 / num2
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except ZeroDivisionError:
            print("Cannot divide by zero! Please enter a non-zero denominator.")
        else:
            print("Result:", result)
            break

divide_numbers()
