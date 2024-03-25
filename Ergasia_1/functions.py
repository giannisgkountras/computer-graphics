import cv2
import numpy as np

def vector_interp(p1, p2, V1, V2, coord, dim):
    """
    Function for computing vector corresponding to point p with linear interpolation

    Args:
        p1 (array): 2D coordinates of point p1.
        p2 (array): 2D coordinates of point p2.
        V1 (array): Vector value corresponding to point p1.
        V2 (array): Vector value corresponding to point p2.
        coord (float): The coordinate (x if dim=1, y if dim=2) of p.
        dim (int): Flag (1 for x coordinate, 2 for y coordinate).

    Returns:
        array: The interpolated vector corresponding to p based on p1 and p2.
    """
    
    if dim == 1:
        if p1[0] < p2[0]:
            x1 = p1[0]
            x2 = p2[0]
        else:
            x1 = p2[0]
            x2 = p1[0]

        width = x2 - x1
        percentage = (coord - x1) / width
        V = np.add(np.multiply((1 - percentage), V1), np.multiply(percentage, V2))

    if dim == 2:
        if p1[1] < p2[1]:
            y1 = p1[1]
            y2 = p2[1]
        else:
            y1 = p2[1]
            y2 = p1[1]

        height = y2 - y1
        percentage = (coord - y1) / height
        V = np.add(np.multiply((1 - percentage), V1), np.multiply(percentage, V2))

    return V
