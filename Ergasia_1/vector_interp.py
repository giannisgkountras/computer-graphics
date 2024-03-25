import cv2
import numpy as np

"""
Function for linear interpolation.

Inputs:
p1 and p2 are the 2-dimensional coordinates of the points of V1 and V2
V1 and V2 are the vector values corresponding to p1 and p2 
coord is either the x position (if dim = 1) or y position if (dim = 2) of point p

Output:
V is the vector value corresponding to p
"""
def vector_interp(p1, p2, V1, V2, coord, dim):
    V = np.array([0, 0])                            # V is initialised as a 2-dimensional zero vector
    V_diff = np.subtract(V1, V2)                    # The vector connecting p1 and p2
    x1 = y1 = x2 = y2 = 0                           # Initialising the latitute and longitude of p1 and p2

    if p1[0] <= p2[0]:
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]                                  # The most left point is considered x1 and y1
    else:
        x1 = p2[0]
        y1 = p2[1]
        x2 = p1[0]
        y2 = p1[1]

    if dim == 1:                                    # We are given x of p
        length = x2 - x1                            # Calculate the difference of x of p1 and p2
        percentage = (coord - x1) / length          # Calculate the percentage of V_diff used to reach p from p1
        V = np.add(V1, percentage * V_diff)         # V is the result of the addition

    if dim == 2:                                    # We are given y of p
        height = abs(y2 - y1)                       # Calculate the difference of y of p1 and p2
        if y2 >= y1:
            percentage = (coord - y1) / height      # Calculate percentage based on the lowest y
        else:
            percentage = (coord - y2) / height
        V = np.add(V1, percentage * V_diff)

    return V                                        # Return the computed vector


p1 = [2, 4]
V1 = [2, 4]
p2 = [8, 3]
V2 = [8, 3]
dim = 1
coord = 4

print(vector_interp(p1,p2,V1,V2,coord,dim))
