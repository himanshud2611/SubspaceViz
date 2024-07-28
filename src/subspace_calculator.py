import numpy as np
from src.matrix_operations import rank

# calculate dimensions of four fundamental spaces
# uses rank-nullity theorem
def column_space(matrix):
    return rank(matrix)

def row_space(matrix):
    return rank(matrix)

def null_space(matrix):
    return matrix.shape[1] - rank(matrix)

def left_null_space(matrix):
    return matrix.shape[0] - rank(matrix)