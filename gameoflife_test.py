import numpy as np
def test():
    matrix = np.zeros([20, 20], dtype=int)
    matrix[0, 1] = 1
    matrix[1, 0] = 1
    matrix[1, 2] = 1
    matrix[2, 0] = 1
    matrix[2, 2] = 1
    matrix[3, 1] = 1
    matrix[3, 2] = 1
    print(matrix)
test()
