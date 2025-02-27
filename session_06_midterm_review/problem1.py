"""
10.0/10.0 points (graded)
Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

This function takes in a list of strings and returns a list of strings. Your function should not modify aList.

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    """
#***************************************************************************
Created on Tue Feb 25 18:18:38 2025

@author: somai
"""
Instructions:
1. Define a function `lessThan4(aList)` that takes a list of strings as input.
2. The function should return a sublist of strings from `aList` that contain fewer than 4 characters.
3. Your function should not modify the original `aList`.

Implementation Steps:
- Iterate through each string in the list.
- Check if the length of the string is less than 4.
- If it is, add it to the result list.
- Return the result list after checking all elements.
"""

#problem 1
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    result = []  # Initialize an empty list to store the result
    
    # Iterate through each string in aList
    for string in aList:
        if len(string) < 4:  # Check if the string has fewer than 4 characters
            result.append(string)  # Add it to the result list
    
    return result  # Return the list of strings with fewer than 4 characters
