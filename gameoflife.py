import numpy as np
import matplotlib.pyplot as plt

class GameofLife():

    def evolve(self, m):
        neigh = m[0, 0] + m[0, 1] + m[0, 2] + m[1, 0] + m[1, 2] + m[2, 0] + m[2, 1] + m[2, 2]
        if neigh == 3:
            center = 1
        elif neigh == 2:
            center = m[1, 1]
        else:
            center = 0
        return center

    def oneStep(self, matrix):
        matrix_shape = np.array(matrix).shape
        expand_matrix = np.pad(matrix, ((1, 1), (1, 1)), 'constant')
        oneStepResult = []
        for i in range(1, matrix_shape[0]+1):
            row = []
            for j in range(1, matrix_shape[1]+1):
                new_cell = expand_matrix[i-1:i+2, j-1:j+2]
                center = self.evolve(new_cell)
                row.append(center)
            oneStepResult.append(row)
        return oneStepResult

    def game(self, matrix, T):
        finalresult = []
        plt.ion()
        for t in range(T):
            matrix = self.oneStep(matrix)
            finalresult.append(matrix)
            plt.imshow(matrix, interpolation='nearest', cmap='gray')
            plt.axis('off')
            plt.pause(0.01)
        plt.ioff()
        plt.show()
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
T = 50
result = s.game(matrix, T)

