import numpy as np
import matplotlib.pyplot as plt
from cell import *


class GameofLife(object):

    def one_step(self, matrix):
        expand_matrix, matrix_shape = self.pad_matrix(matrix)
        oneStepResult = []
        for i in range(1, matrix_shape[0]+1):
            row = []
            for j in range(1, matrix_shape[1]+1):
                new_cell = expand_matrix[i-1:i+2, j-1:j+2]
                center = Cell().evolve(new_cell)
                row.append(center)
            oneStepResult.append(row)
        return oneStepResult

    def pad_matrix(self, matrix):
        matrix_shape = np.array(matrix).shape
        expand_matrix = np.pad(matrix, ((1, 1), (1, 1)), 'constant')
        return expand_matrix, matrix_shape

    def game(self, matrix, T, interval):
        finalresult = []
        plt.ion()
        for t in range(T):
            matrix = self.one_step(matrix)
            finalresult.append(matrix)
            plt.imshow(matrix, interpolation='nearest', cmap='gray')
            plt.axis('off')
            plt.pause(interval)
        plt.ioff()
        plt.show()
        return finalresult


if __name__ == '__main__':
    s = GameofLife()
    screen_row = int(input("请输入画布的行数："))
    screen_column = int(input("\n请输入画布的列数："))
    matrix = np.zeros([screen_row, screen_column], dtype=int)
    cell_number = int(input('\n请输入存活细胞数量:'))
    print('\n请输入存活细胞坐标，从1开始计数，如 1 1:')
    for n in range(cell_number):
        i, j = map(int, input('第 {} 个坐标:'.format(n+1)).split())
        matrix[i-1, j-1] = 1
    T = int(input("\n请输入迭代次数："))
    interval = float(input('\n请输入停顿时间，如0.01：'))
    print("\n您所输入的初始状态为：\n{}".format(matrix))
    result = s.game(matrix, T, interval)



