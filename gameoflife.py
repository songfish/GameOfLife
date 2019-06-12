import numpy as np
import matplotlib as plt

class GameofLife():
    def game(self, matrix):
        matrix_shape = matrix.shape
        expand_matrix = np.pad(matrix, ((1, 1), (1, 1)), 'constant')

        def evolve(m):
            neigh = m[0, 0] + m[0, 1] + m[0, 2] + m[1, 0] + m[1, 2] + m[2, 0] + m[2, 1] + m[2, 2]
            if neigh == 3:
                center = 1
            elif neigh == 2:
                center = m[1, 1]
            else:
                center = 0
            return center

        finalresult = []
        for i in range(1, matrix_shape[0]+1):
            row = []
            for j in range(1, matrix_shape[1]+1):
                new_cell = expand_matrix[i-1:i+2, j-1:j+2]
                center = evolve(new_cell)
                row.append(center)
            finalresult.append(row)
        return finalresult


s = GameofLife()
matrix = np.zeros([20, 20], dtype=int)
matrix[0, 1] = 1
matrix[1, 0] = 1
matrix[1, 2] = 1
matrix[2, 0] = 1
matrix[2, 2] = 1
matrix[3, 1] = 1
matrix[3, 2] = 1
result = s.game(matrix)
print(np.array(result))
