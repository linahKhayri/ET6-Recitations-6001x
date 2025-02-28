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
#problem 3
def score(word, f):
    """
    word: a string of length > 1 of alphabetical characters (upper and lowercase)
    f: a function that takes in two int arguments and returns an int
    
    Returns the score of the word as defined by the method:
    1) The score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from the start of the word.
    2) The final score for the word is the result of applying `f` to the scores
    of the two highest scoring letters in the word.
       The first parameter to `f` is the highest letter score, and the second 
       parameter is the second highest letter score.
    """
    
    # Define a dictionary to map letters to their position in the alphabet
    alphabet = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }
    
    # Calculate the letter scores for the word
    letter_scores = []
    index = 0  # Start with the first index (0)
    
    for letter in word:
        # Convert letter to lowercase and get its position from the alphabet dictionary
        letter_value = alphabet[letter.lower()]
        letter_scores.append(letter_value * index)  # Multiply by its distance from the start of the word
        index += 1  # Move to the next index
    
    # Sort the letter scores in descending order
    letter_scores.sort(reverse=True)
    
    # Apply the function `f` to the two highest scores (if there are at least two letters)
    return f(letter_scores[0], letter_scores[1])

# Example function to test score
def sum_scores(a, b):
    return a + b

# Example usage:
print(score('adD', sum_scores))  # Output will be 12 (1*0 + 4*1 + 4*2 => highest 4*2 = 8, second highest 4*1 = 4, sum = 12
    """
# another solution
def score(word, f):
   
    scoreList=[]    #contains list of score of individual word
    for index in range(len(word)):
        char = word[index].upper()
        score = index * (ord(char)%64)          #using ascii code for getting a=1, b=2 ....
        scoreList.append(score)
    scoreList.sort(reverse=True)                #the 1st 2 elements of list have highest score
    return f(scoreList[0],scoreList[1])
    """
# Hasan Zemzem' Group 
def f(h1, h2):
    """
    A function to return the sum of two numbers
    """
    return h1 + h2

def score(word, f):
    
    # Define a dictionary to map letters to their position in the alphabet
    alphabet_position = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }
    
    word_lower = word.lower()
    scores = []
    for i in range(len(word_lower)):
        scores.append(i * alphabet_position[word_lower[i]])
    scores.sort()
    
    return f(scores[-1], scores[-2])

# Example usage:
print(score('Somaia', f))


# Solara Hamza' Group
def score(word, f):
    alpha={}
    position=1
    for char in "abcdefghijklmnopqrstuvwxyz":
        alpha[char]=position
        position+=1
    letter_scores=[]
    for index in range(len(word)):
        letter_lower=word[index].lower()
        letter_position=alpha[letter_lower]
        score_value= letter_position * index
        letter_scores.append(score_value)
    letter_scores.sort(reverse=True)
    return (f(letter_scores[0],letter_scores[1]))
def f(x,y):
        return x+y

# Said Ibrahim's Group 
def score(word, f):
    # List to store all scores
    scores = []
    # Calculate score for each letter
    for i in range(len(word)):
        # Get alphabet position (1-26)
        char = word[i].lower()
        alpha_pos = ord(char) - ord('a') + 1
        # Multiply by distance from start
        letter_score = alpha_pos * i
        scores.append(letter_score)
    
    # Sort scores in descending order
    scores.sort(reverse=True)
    
    # Return f applied to two highest scores
    return f(scores[0], scores[1])


def add(a, b):
    return a + b
