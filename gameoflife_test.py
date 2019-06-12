from gameoflife_1 import *
import numpy as np
import unittest


class TestGameFunc(unittest.TestCase):
    def test_evolve(self):
        m1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.assertEqual(0, evolve(m1))

        m2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(1, evolve(m2))

        m3 = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
        self.assertEqual(0, evolve(m3))

        m4 = np.array([[1, 0, 1], [0, 0, 0], [0, 0, 1]])
        self.assertEqual(1, evolve(m4))

        m5 = np.array([[1, 0, 1], [0, 0, 1], [0, 0, 1]])
        self.assertEqual(0, evolve(m5))


if __name__ == '__main__':
    unittest.main()
