import numpy as np

def make_table(rows:int, columns:int) -> list[list[int]] :
    return np.arange(rows * columns).reshape(rows,columns).tolist

def rectangle(matrix : list[list[int]], row_start : int, row_stop : int, column_start : int, column_stop : int) -> list[list[int]]:
    return np.array(matrix)[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix : list[list[int]], row_start : int, row_stop : int, column_start : int, column_stop : int, value:int) -> list[list[int]]:
    arr = np.array(matrix).copy
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()

def matrix_vector_product(matrix, vector) -> list[list[int]]:
    return (np.array(matrix) @ np.array(vector)).tolist()

def matrix_multiply(left, right) -> list[list[int]]:
    return (np.array(left) @ np.array(right)).tolist()

def transpose_matrix(matrix) -> list[list[int]]:
    return np.array(matrix).T.tolist()

def solve_system(matrix, vector) -> list[list[int]]:
    return np.linalg.solve(np.array(matrix) @ np.array(vector))

def tensor_channel_mean(tensor) -> list[list[int]]:
    return np.array(tensor).mean(axis=-1).tolist()
    
def point_distance(first, second) -> list[list[int]]:
    return np.linalg.norm(np.array(first) - np.array(second))