from gameoflife import *
import numpy as np
import unittest


class TestGameFunc(unittest.TestCase):

    def test_evolve(self):
        s = GameofLife()
        self.one_cell(s)
        self.two_cells(s)
        self.three_cells(s)
        self.more_cells(s)

    def one_cell(self, s):
        m1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.assertEqual(0, s.evolve(m1))

    def two_cells(self, s):
        m2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(1, s.evolve(m2))

    def three_cells(self, s):
        m3 = np.array([[1, 0, 1], [0, 0, 0], [0, 0, 1]])
        self.assertEqual(1, s.evolve(m3))

    def more_cells(self, s):
        m4 = np.array([[1, 0, 1], [0, 0, 1], [0, 0, 1]])
        self.assertEqual(0, s.evolve(m4))








if __name__ == '__main__':
    unittest.main()
