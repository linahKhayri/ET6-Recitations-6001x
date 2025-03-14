# **🔹 Exercise 2: Fix Bubble Sort**
# Identify and fix the bug

def bubble_sort(L):
    n = len(L)
    for i in range(n):
        for j in range(n - 1):  #  There’s an inefficiency here!
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L

arr = [5, 3, 8, 4, 2]
print(bubble_sort(arr))  # Expected output: [2, 3, 4, 5, 8]
