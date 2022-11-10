"""
Write a Python function mult(M, N) that computes the matrix multiplication between the matrices of integers M and N, in that order.
When the matrices' dimensions are not compatible, the function must return an empty list.

You cannot use numpy.
"""

def mult(M, N):
    if len(M[0]) != len(N):
        return []
    result = [[sum(a*b for a,b in zip(M_row,N_col)) for N_col in zip(*N)] for M_row in M]
    return result

print(mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
# [[4, 4], [10, 8]]
print(mult([[1, 2, 3], [4, 5, 6]], [[9], [8], [7]]))
# [[46], [118]]
print(mult([[7, 8, 9, 10]], [[5], [3], [2], [7]]))
# [[147]]
print(mult([[1, 2], [3, 4]], [[5], [6], [7]]))
# []