class Cell(object):

    def evolve(self, m):
        neigh = m[0, 0] + m[0, 1] + m[0, 2] + m[1, 0] + m[1, 2] + m[2, 0] + m[2, 1] + m[2, 2]
        if neigh == 3:
            center = 1
        elif neigh == 2:
            center = m[1, 1]
        else:
            center = 0
        return center
