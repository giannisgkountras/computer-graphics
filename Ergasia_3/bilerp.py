import numpy as np
from vector_interp import vector_interp


def bilerp(uv, texture_map):

    # Extract the dimensions of the texture map
    height, width, _ = texture_map.shape

    # Extract the uv coordinates
    u, v = uv

    # Calculate the positions and indices of the four corners

    x = u * (width - 1)
    y = v * (height - 1)

    x1 = int(np.floor(x))
    x2 = min(x1 + 1, width - 1)
    y1 = int(np.floor(y))
    y2 = min(y1 + 1, height - 1)

    # Calculate the fractional parts
    dx = x - x1
    dy = y - y1

    # Fetch the values at the corners
    Q11 = texture_map[y1, x1]
    Q12 = texture_map[y2, x1]
    Q21 = texture_map[y1, x2]
    Q22 = texture_map[y2, x2]

    # Perform the bilinear interpolation
    R1 = (1 - dx) * Q11 + dx * Q21
    R2 = (1 - dx) * Q12 + dx * Q22
    P = (1 - dy) * R1 + dy * R2

    # Clip values to ensure they are within [0, 1]
    # P = np.clip(P, 0, 1)
    return P
