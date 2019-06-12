from gameoflife_1 import *
import numpy as np
import unittest


class TestGameFunc(unittest.TestCase):
    def test_evolve(self):
        # matrix = np.zeros([20, 20], dtype=int)
        # matrix[0, 1] = 1
        # matrix[1, 0] = 1
        # matrix[1, 2] = 1
        # matrix[2, 0] = 1
        # matrix[2, 2] = 1
        # matrix[2, 3] = 1
        # matrix[3, 1] = 1
        # matrix[3, 2] = 1
        # expected_result = np.pad(matrix, ((1, 1), (1, 1)), 'constant')
        # self.assertEqual(expected_result, evolve())

        # 1 neighbor
        m1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.assertEqual(0, evolve(m1))

        m2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(1, evolve(m2))

        m2 = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
        self.assertEqual(0, evolve(m2))


if __name__ == '__main__':
    unittest.main()
