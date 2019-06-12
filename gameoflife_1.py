def evolve(m):
    neigh = m[0, 0] + m[0, 1] + m[0, 2] + m[1, 0] + m[1, 2] + m[2, 0] + m[2, 1] + m[2, 2]
    if neigh == 3:
        result = 1
    elif neigh == 2:
        result = m[1, 1]
    else:
        result = 0
    return result
