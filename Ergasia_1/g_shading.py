from vector_interp import vector_interp


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
        "slope": (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float("inf"),
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
        "slope": (y3 - y2) / (x3 - x2) if (x3 - x2) != 0 else float("inf"),
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
        "slope": (y1 - y3) / (x1 - x3) if (x1 - x3) != 0 else float("inf"),
        "top_color": vcolors[2] if y3 > y1 else vcolors[0],
        "bottom_color": vcolors[0] if y3 > y1 else vcolors[2],
        "vertices": [[x3, y3], [x1, y1]],
    }

    edges = [edge1, edge2, edge3]

    y_min_total = min(y1, y2, y3)
    y_max_total = max(y1, y2, y3)

    active_edges = []
    active_points_colors = []

    for y in range(y_min_total, y_max_total + 1):
        active_edges = [edge for edge in active_edges if not (edge["y_max"] < y)]

        for edge in edges:
            if edge["y_min"] == y and edge["y_max"] != edge["y_min"]:
                active_edges.append(edge)
            elif edge["y_max"] == y and edge in active_edges:
                active_edges.remove(edge)

        active_points_colors = []

        for active_edge in active_edges:
            color = vector_interp(
                [0, active_edge["y_min"]],  # We dont care about x
                [0, active_edge["y_max"]],
                active_edge["bottom_color"],
                active_edge["top_color"],
                y,
                2,
            )

            if active_edge["slope"] > 0:
                active_points_colors.append(
                    [
                        [
                            active_edge["x_min"]
                            + (1 / active_edge["slope"]) * (y - active_edge["y_min"]),
                            y,
                        ],
                        color,
                    ]
                )

            elif active_edge["slope"] < 0:
                active_points_colors.append(
                    [
                        [
                            active_edge["x_max"]
                            + (1 / active_edge["slope"]) * (y - active_edge["y_min"]),
                            y,
                        ],
                        color,
                    ]
                )

            elif active_edge["slope"] == 0 and y == y_min_total:
                pass

            elif active_edge["slope"] == float("inf"):
                active_points_colors.append([[active_edge["x_min"], y], color])

        active_points_colors = sorted(active_points_colors, key=lambda x: x[0][0])

        if len(active_points_colors) == 2:
            for x in range(
                round(active_points_colors[0][0][0]),
                round(active_points_colors[1][0][0]),
            ):
                color = vector_interp(
                    [active_points_colors[0][0][0], 0],  # y is dont care so 0
                    [active_points_colors[1][0][0], 0],  # y is dont care so 0
                    active_points_colors[0][1],
                    active_points_colors[1][1],
                    x,
                    1,
                )
                img[y][x] = color

    return img
