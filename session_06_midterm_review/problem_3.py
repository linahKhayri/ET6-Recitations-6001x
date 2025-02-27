"""10.0/10.0 points (graded)
Write a function called score that meets the specifications below.

def score(word, f):
    
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    #YOUR CODE HERE
    #*****************************************************************
    """
Created on Tue Feb 25 18:18:38 2025
@author: somai

Instructions:
1. Define a function `score(word, f)` that takes a string `word` and a function `f` as input.
2. The `word` is a string of length greater than 1, consisting of alphabetical characters (both uppercase and lowercase).
3. The function `f` is a function that takes in two integer arguments and returns an integer.
   
4. The scoring process involves:
   a) Calculating the score for each letter in the word based on its position in the alphabet (a = 1, b = 2, ..., z = 26).
      The score for each letter is calculated as:
      - `letter_score = letter_position_in_alphabet * index_in_word`
      For example, for the word "adD":
      - 'a' has position 1, and is at index 0, so its score is `1 * 0 = 0`.
      - 'd' has position 4, and is at index 1, so its score is `4 * 1 = 4`.
      - 'D' has position 4 (same as 'd'), and is at index 2, so its score is `4 * 2 = 8`.
    
   b) Find the two highest letter scores from the word. These scores will be the two highest values in the list of letter scores.
   
5. The final score of the word is calculated by applying the function `f` to the two highest letter scores. The first argument to `f` is the highest score, and the second argument is the second-highest score.

Implementation Steps:
- Initialize an empty list `letter_scores` to store the letter scores.
- Iterate through each letter in the word. For each letter:
  - Find its position in the alphabet by using a dictionary and multiply it by its index in the word.
  - Append the result to `letter_scores`.
- Sort `letter_scores` in descending order to get the highest scores at the front.
- Apply the function `f` to the two highest scores and return the result.

Example:
For the word 'adD', the letter scores are [0, 4, 8]. The highest scores are 8 and 4.
If `f` is the sum of its arguments, then the final score would be:
f(8, 4) = 12
"""
#def score(word, f):
    """
    word: a string of length > 1 of alphabetical characters (upper and lowercase)
    f: a function that takes in two int arguments and returns an int
    
    Returns the score of the word as defined by the method:
    1) The score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from the start of the word.
    2) The final score for the word is the result of applying `f` to the scores of the two highest scoring letters in the word.
       The first parameter to `f` is the highest letter score, and the second parameter is the second highest letter score.
    """
    
    # Define a dictionary to map letters to their position in the alphabet
  
    
    # Calculate the letter scores for the word
    
    # Start with the first index (0)
    
    
    
        # Convert letter to lowercase and get its position from the alphabet dictionary
       
        # Multiply by its distance from the start of the word
     
        # Move to the next index
    
          # Sort the letter scores in descending order
   
    
    # Apply the function `f` to the two highest scores (if there are at least two letters)
    

# Example function to test score


# Example usage:

# Output will be 12 (1*0 + 4*1 + 4*2 => highest 4*2 = 8, second highest 4*1 = 4, sum = 12)
