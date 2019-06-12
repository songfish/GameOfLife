import numpy as np


def evolve(m):
    # m = np.zeros([3, 3], dtype=int)
    neigh = m[0, 0] + m[0, 1] + m[0, 2] + m[1, 0] + m[1, 2] + m[2, 0] + m[2, 1] + m[2, 2]
    if neigh == 3:
        m[1, 1] = 1
    if neigh == 2:
        m[1, 1] = m[1, 1]
    else:
        m[1, 1] = 0
    return m[1, 1]
