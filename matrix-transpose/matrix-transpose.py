import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    # result = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

    result = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            result[j][i] = A[i][j]
    return np.array(result)
