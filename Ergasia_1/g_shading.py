import numpy as np
import math
from vector_interp import vector_interp


def point_belongs_to_edge(point, edge):
    """
    Check if a given point belongs to a given edge.

    Args:
    point (array): The coordinates of the point in the form [x, y].
    edge (dict): The edge represented as a dictionary with the following keys:
        - "x_min" (float): The minimum x-coordinate of the edge's bounding box.
        - "x_max" (float): The maximum x-coordinate of the edge's bounding box.
        - "y_min" (float): The minimum y-coordinate of the edge's bounding box.
        - "y_max" (float): The maximum y-coordinate of the edge's bounding box.
        - "vertices" (list): The vertices of the edge represented as a list of tuples (x, y).

    Returns:
    bool: True if the point belongs to the edge, False otherwise.
    """
    x, y = point
    x_min, x_max = edge["x_min"], edge["x_max"]
    y_min, y_max = edge["y_min"], edge["y_max"]

    # Check if point lies within the bounding box of the edge
    if x < x_min or x > x_max or y < y_min or y > y_max:
        return False

    # Check if point lies on the line segment formed by the edge's vertices
    x1, y1 = edge["vertices"][0]
    x2, y2 = edge["vertices"][1]

    # Calculate the slope of the edge
    slope = edge["slope"]

    # If the edge is vertical, check if the x-coordinate of the point matches
    if slope == math.inf:
        return x == x1

    # Calculate the expected y-coordinate of the point on the edge
    expected_y = y1 + slope * (x - x1)

    # Check if the actual y-coordinate matches the expected y-coordinate
    return math.isclose(y, expected_y)


def g_shading(img, vertices, vcolors):
    """
    This image gives each of the triangle's pixels the interpolated vector of the 3 apex colors.

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

    # Define the edges
    edge1 = {
        "name": "Edge 1",
        "x_min": min(x1, x2),
        "x_max": max(x1, x2),
        "y_min": min(y1, y2),
        "y_max": max(y1, y2),
        # If x2 - x1 is zero set the slope to infinity
        "slope": (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else math.inf,
        "top_color": vcolors[0] if y1 > y2 else vcolors[1],
        "bottom_color": vcolors[1] if y1 > y2 else vcolors[0],
        "vertices": [[x1, y1], [x2, y2]],
    }

    # Edge one is between vertex 2 and 3
    edge2 = {
        "name": "Edge 2",
        "x_min": min(x2, x3),
        "x_max": max(x2, x3),
        "y_min": min(y2, y3),
        "y_max": max(y2, y3),
        # If x3 - x2 is zero set the slope to infinity
        "slope": (y3 - y2) / (x3 - x2) if (x3 - x2) != 0 else math.inf,
        "top_color": vcolors[1] if y2 > y3 else vcolors[2],
        "bottom_color": vcolors[2] if y2 > y3 else vcolors[1],
        "vertices": [[x2, y2], [x3, y3]],
    }

    # Edge one is between vertex 3 and 1
    edge3 = {
        "name": "Edge 3",
        "x_min": min(x3, x1),
        "x_max": max(x3, x1),
        "y_min": min(y3, y1),
        "y_max": max(y3, y1),
        # If x1 - x1 is zero set the slope to infinity
        "slope": (y1 - y3) / (x1 - x3) if (x1 - x3) != 0 else math.inf,
        "top_color": vcolors[2] if y3 > y1 else vcolors[0],
        "bottom_color": vcolors[0] if y3 > y1 else vcolors[2],
        "vertices": [[x3, y3], [x1, y1]],
    }

    # Array of edges
    edges = [edge1, edge2, edge3]

    # Find the minimum y of all edges
    y_min_total = min(edge["y_min"] for edge in edges)

    # Find the maximum y of all edges
    y_max_total = max(edge["y_max"] for edge in edges)

    # Initialise active_edges as an empty array
    active_edges = []

    # Initialise active_points as an empty array
    active_points = []

    # Implementation of the scanline
    for y in range(y_min_total, y_max_total + 1):
        # We use the convention that the lowest vertex does belong in the triangle but the top does not
        for edge in edges:
            # Add an edge to active_edges as soon as y reaches its y_min
            if edge["y_min"] == y:
                active_edges.append(edge)
            # Remove an edge from active_edges when we reach its max
            if edge["y_max"] <= y and edge in active_edges:
                active_edges.remove(edge)
            # Handle horizontal edges using the convention that they belong in the top triangle
            if edge["y_min"] == edge["y_max"] and y == y_min_total:
                active_edges.append(edge)

        # Reset active points
        active_points = []

        # Caclculate new active points
        for active_edge in active_edges:
            # Handle vertical active edges
            if active_edge["slope"] == math.inf:
                active_points.append([active_edge["x_min"], y])

            # Handle positive slope active edges
            elif active_edge["slope"] > 0:
                active_points.append(
                    [
                        active_edge["x_min"]
                        + (1 / active_edge["slope"]) * (y - active_edge["y_min"]),
                        y,
                    ]
                )

            # Handle negative slope active edges
            elif active_edge["slope"] < 0:
                active_points.append(
                    [
                        active_edge["x_max"]
                        + (1 / active_edge["slope"]) * (y - active_edge["y_min"]),
                        y,
                    ]
                )

        # Remove dublicate points from active points:
        unique_active_points = []
        for point in active_points:
            if point not in unique_active_points:
                unique_active_points.append(point)

        # Sort active points based on x
        sorted_active_points = sorted(unique_active_points, key=lambda x: x[0])

        if len(active_edges) > 1:
            if point_belongs_to_edge(sorted_active_points[0], active_edges[0]):
                left_edge = active_edges[0]
                right_edge = active_edges[1]
            else:
                left_edge = active_edges[1]
                right_edge = active_edges[0]

            # Interpolate colors for the left and right edges
            color_left = vector_interp(
                [0, left_edge["y_min"]],
                [0, left_edge["y_max"]],
                left_edge["bottom_color"],
                left_edge["top_color"],
                y,
                2,
            )

            color_right = vector_interp(
                [0, right_edge["y_min"]],
                [0, right_edge["y_max"]],
                right_edge["bottom_color"],
                right_edge["top_color"],
                y,
                2,
            )

        if len(sorted_active_points) == 1:
            color = [0, 0, 0]
            img[y, math.floor(sorted_active_points[0][0])] = np.array(color)
        elif len(sorted_active_points) > 1:
            for x in range(
                math.floor(sorted_active_points[0][0]),
                math.floor(sorted_active_points[1][0]),
            ):
                color = vector_interp(
                    [sorted_active_points[0][0], 0],
                    [sorted_active_points[1][0], 0],
                    color_left,
                    color_right,
                    x,
                    1,
                )
                img[y][x] = np.array(color)

    return img
