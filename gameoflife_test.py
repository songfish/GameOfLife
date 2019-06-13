from gameoflife import *
from cell import *
import numpy as np
import unittest


class TestGameFunc(unittest.TestCase):

    def test_evolve(self):
        c = Cell()
        self.one_neighbor(c)
        self.two_neighbors(c)
        self.three_neighbors(c)
        self.more_neighbors(c)

    def one_neighbor(self, s):
        m1 = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(0, s.evolve(m1))

    def two_neighbors(self, s):
        m2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(1, s.evolve(m2))

    def three_neighbors(self, s):
        m3 = np.array([[1, 0, 1], [0, 0, 0], [0, 0, 1]])
        self.assertEqual(1, s.evolve(m3))

    def more_neighbors(self, s):
        m4 = np.array([[1, 0, 1], [0, 0, 1], [0, 0, 1]])
        self.assertEqual(0, s.evolve(m4))








if __name__ == '__main__':
    unittest.main()
