def f_shading(img, vertices, vcolors):
    """
    This image gives triangles the vector mean of the 3 apex colors.

    Args:
        img (MxNx3 array): The image with previously existing triangles
        vertices (3x2 array): Each row contains the 2D coordinates of an apex of a triangle
        vcolors (3x3 array): Each row contains the color of the corresponding point in RGB [0,1]

    Returns
        MxNx3 array: The updated image with RGB for each pixel of the triangle plus the old image (overlapping common pixels)

    """

    # Calculate the color of the triangle
    color = [(vcolors[0][i] + vcolors[1][i] + vcolors[2][i]) / 3 for i in range(3)]

    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]

    # Define the edges as dictionaries
    edge1 = {
        "name": "Edge 1",
        "x_min": min(x1, x2),
        "x_max": max(x1, x2),
        "y_min": min(y1, y2),
        "y_max": max(y1, y2),
        # If x2 - x1 is zero set the slope to infinity
        "slope": (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float("inf"),
    }

    edge2 = {
        "name": "Edge 2",
        "x_min": min(x2, x3),
        "x_max": max(x2, x3),
        "y_min": min(y2, y3),
        "y_max": max(y2, y3),
        # If x3 - x2 is zero set the slope to infinity
        "slope": (y3 - y2) / (x3 - x2) if (x3 - x2) != 0 else float("inf"),
    }

    edge3 = {
        "name": "Edge 3",
        "x_min": min(x3, x1),
        "x_max": max(x3, x1),
        "y_min": min(y3, y1),
        "y_max": max(y3, y1),
        # If x1 - x3 is zero set the slope to infinity
        "slope": (y1 - y3) / (x1 - x3) if (x1 - x3) != 0 else float("inf"),
    }

    edges = [edge1, edge2, edge3]

    # Calculate the y_min and y_max of the triangle
    y_min_total = min(y1, y2, y3)
    y_max_total = max(y1, y2, y3)

    # Initialise active edges and active points as empy arrays
    active_edges = []
    active_points = []

    # Implement the moving scanline
    for y in range(y_min_total, y_max_total + 1):
        for edge in edges:

            # Append new active edges if they are not horizontal
            if edge["y_min"] == y and edge["y_max"] != edge["y_min"]:
                active_edges.append(edge)

            # Remove no longer active edges
            elif edge["y_max"] == y and edge in active_edges:
                active_edges.remove(edge)

        # Reset active points for given y
        active_points = []

        # Calculate active points using the slope of the edge and current y
        for active_edge in active_edges:
            if active_edge["slope"] > 0:
                active_points.append(
                    [
                        active_edge["x_min"]
                        + (1 / active_edge["slope"]) * (y - active_edge["y_min"]),
                        y,
                    ]
                )

            elif active_edge["slope"] < 0:
                active_points.append(
                    [
                        active_edge["x_max"]
                        + (1 / active_edge["slope"]) * (y - active_edge["y_min"]),
                        y,
                    ]
                )

            # When slope == 0 we add no active points because the points of the horizontal
            # edge are already calculated in the other 2 edges that contain them.
            elif active_edge["slope"] == 0 and y == y_min_total:
                pass

            elif active_edge["slope"] == float("inf"):
                active_points.append([active_edge["x_min"], y])

        # Sort active points from leftest to rightest
        active_points = sorted(active_points, key=lambda x: x[0])

        # Draw on the image for all intermediate points
        if len(active_points) == 2:
            # The array active_points looks like this: [[x1,y1],[x2,y2]]
            # The range of the loop is from x1 to x2
            for x in range(round(active_points[0][0]), round(active_points[1][0])):
                img[y][x] = color
    return img
