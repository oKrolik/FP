"""
A magic square is a matrix of n*n integer numbers such that every line, column and two diagonals sum the same value.

Define a function magic(mat) that tests if a matrix mat (represented by a list of lists of integers) is a magic square. 
The matrix can have any square dimensions n*n such that n>=3. 
The result returned by the function should be a Boolean value: True if the matrix is a magic square and False otherwise.

Note: Your code must pass all tests (all-or-nothing) to get a grade.
"""

def magic(matrix):
    sumD1 = 0
    sumD2 = 0
    for i in range(len(matrix)):
        sumD1 += matrix[i][i]
        sumD2 += matrix[i][len(matrix)-i-1]
    if not(sumD1 == sumD2):
            return False
    for i in range(len(matrix)):
        sumR = 0
        sumC = 0
        for j in range(len(matrix)):
            sumR += matrix[i][j]
            sumC += matrix[j][i]
        if not(sumR == sumC == sumD1):
            return False
    return True

print(magic([[8, 1, 6], [3, 5, 7], [4, 9, 2]])) # True
print(magic([[8, 1, 6], [3, 6, 7], [4, 9, 2]])) # False
print(magic([[16, 2, 12], [6, 10, 14], [8, 18, 4]])) # True
print(magic([[8, 3, 4], [1, 5, 9], [6, 7, 2]])) # True
print(magic([[9, 1, 6], [3, 6, 7], [4, 9, 3]])) # False
print(magic([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])) # True
print(magic([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [5, 7, 14, 21, 23], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])) # False
print(magic([[17, 24, 2, 8, 15], [23, 5, 8, 14, 16], [4, 6, 14, 20, 22], [10, 12, 20, 21, 3], [11, 18, 26, 2, 9]])) # False
print(magic([[16, 2, 12], [6, 10, 14], [8, 18, 4]])) # True
print(magic([[34, 48, 2, 16, 30], [46, 10, 14, 28, 32], [8, 12, 26, 40, 44], [20, 24, 38, 42, 6], [22, 36, 50, 4, 18]])) # True
print(magic([[18, 24, 1, 8, 15], [23, 6, 7, 14, 16], [4, 6, 14, 20, 22], [10, 12, 19, 22, 3], [11, 18, 25, 2, 10]])) # False
print(magic([[17, 24, 1, 8, 16], [23, 5, 7, 15, 16], [4, 6, 14, 20, 22], [10, 13, 19, 21, 3], [12, 18, 25, 2, 9]])) # False
print(magic([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [5, 7, 14, 21, 23], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])) # False
print(magic([[17, 24, 2, 8, 15], [23, 5, 8, 14, 16], [4, 6, 14, 20, 22], [10, 12, 20, 21, 3], [11, 18, 26, 2, 9]])) # False
print(magic([[1, 1, 1], [0, 0, 0], [2, 2, 2]])) # False
print(magic([[1, 1, 1], [1, 2, 0], [1, 0, 2]])) # False
print(magic([[1, 0, 2], [1, 0, 2], [1, 0, 2]])) # False