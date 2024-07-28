import numpy as np

def matrix_mul(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def transpose(matrix):
    return np.transpose(matrix)

def rank(matrix):
    return np.linalg.matrix_rank(matrix)