from gameoflife import *
import numpy as np
import unittest


class TestGameFunc(unittest.TestCase):
    def test_evolve(self):
        s = GameofLife()
        m1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.assertEqual(0, s.evolve(m1))

        m2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(1, s.evolve(m2))

        m3 = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
        self.assertEqual(0, s.evolve(m3))

        m4 = np.array([[1, 0, 1], [0, 0, 0], [0, 0, 1]])
        self.assertEqual(1, s.evolve(m4))

        m5 = np.array([[1, 0, 1], [0, 0, 1], [0, 0, 1]])
        self.assertEqual(0, s.evolve(m5))


if __name__ == '__main__':
    unittest.main()
