import numpy as np
def evolve():
    # init state
    matrix = np.zeros([20, 20], dtype=int)
    matrix[0, 1] = 1
    matrix[1, 0] = 1
    matrix[1, 2] = 1
    matrix[2, 0] = 1
    matrix[2, 2] = 1
    matrix[3, 1] = 1
    matrix[3, 2] = 1
    # expand_matrix = np.pad(matrix, ((1, 1), (1, 1)), 'constant')
    m = np.pad(matrix, ((1, 1), (1, 1)), 'constant')
    # m = expand_matrix
    expand_matrix = m
    print(expand_matrix)
    for i in range(1, 21):
        for j in range(1, 21):
            neigh = m[i-1, j-1] + m[i-1, j] + m[i-1, j+1] + m[i, j-1] + m[i, j+1] + m[i+1, j-1] \
                    + m[i+1, j] + m[i+1, j+1]
            if neigh == 3:
                expand_matrix[i, j] = 1
            elif neigh == 2:
                expand_matrix[i, j] = m[i, j]
            else:
                expand_matrix[i, j] = 0
    return neigh

evolve()