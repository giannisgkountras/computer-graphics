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
        # Check which point is more left and name its x coordinate x1
        if p1[0] < p2[0]:
            x1 = p1[0]
            x2 = p2[0]
            V_left = V1
            V_right = V2
        else:
            # In the case of p2 beeing more left than p1 we name x1
            # the x coordinate of p2 and also swap the vectors
            x1 = p2[0]
            x2 = p1[0]
            V_left = V2
            V_right = V1
        # Calculate the distance between the points on the x axis
        width = x2 - x1

        # Calculate what percentage of width is the distance on the
        # x axis between p and the most left point
        percentage = (coord - x1) / width

        # Calculate the final vector by doing a linear interpolation
        # using the percentage and V_left and V_right. Since the percentage is calculated based
        # on the most left point, we use (1 - percentage) for V_left
        V = np.add(
            np.multiply((1 - percentage), V_left), np.multiply(percentage, V_right)
        )

    if dim == 2:
        # Check which point is more down and name its y coordinate y1
        if p1[1] < p2[1]:
            y1 = p1[1]
            y2 = p2[1]
            V_down = V1
            V_up = V2
        else:
            # In the case of p2 beeing more down than p1 we name y1
            # the y coordinate of p2 and also swap the vectors
            y1 = p2[1]
            y2 = p1[1]
            V_down = V2
            V_up = V1
        # Calculate the distance between the points on the y axis
        height = y2 - y1

        # Calculate what percentage of height is the distance on the
        # y axis between p and the most down point
        percentage = (coord - y1) / height

        # Calculate the final vector by doing a linear interpolation
        # using the percentage and V_down and V_up. Since the percentage is calculated based
        # on the most down point, we use (1 - percentage) for V_down
        V = np.add(np.multiply((1 - percentage), V_down), np.multiply(percentage, V_up))

    return V


def f_shading(img, vertices, vcolors):
    """
    This image gives triangles the vector mean of the 3 apex colors.

    Args:
        img (MxNx3 array): The image with previously existing triangles
        vertices (3x2 array): Each row contains the 2D coordinates of an apex of a triangle
        vcolors (3x3 array): Each row contains the color of the corresponding point in RGB [0,1]

    Returns
        MxNx3 array: The updated image with RGB for each pixel plus the old image (overlapping common pixels)

    """
    pass
