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
    # Save coordinates of each vertex
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]

    # Edge one is between vertex 1 and 2
    edge1 = {
        "name": "Edge 1",
        "x_min": min(x1, x2),
        "x_max": max(x1, x2),
        "y_min": min(y1, y2),
        "y_max": max(y1, y2),
    }

    # Edge one is between vertex 2 and 3
    edge2 = {
        "name": "Edge 2",
        "x_min": min(x2, x3),
        "x_max": max(x2, x3),
        "y_min": min(y2, y3),
        "y_max": max(y2, y3),
    }

    # Edge one is between vertex 3 and 1
    edge3 = {
        "name": "Edge 3",
        "x_min": min(x3, x1),
        "x_max": max(x3, x1),
        "y_min": min(y3, y1),
        "y_max": max(y3, y1),
    }

    # Array of edges
    edges = [edge1, edge2, edge3]

    # Find the minimum y of all edges
    y_min_total = min(edge["y_min"] for edge in edges)

    # Find the maximum y of all edges
    y_max_total = max(edge["y_max"] for edge in edges)

    # Initialise active_edges as an empty array
    active_edges = []

    # Update the active edges for moving scanline
    for y in range(y_min_total, y_max_total + 1):
        # We use the convention that the lowest vertex does belong in the triangle but the top does not
        for edge in edges:
            if edge["y_min"] == y:
                active_edges.append(edge)
            if edge["y_max"] == y:
                active_edges.remove(edge)

        print("For scanline ", y, " Active edges are: ")
        for active_edge in active_edges:
            print(active_edge["name"])
