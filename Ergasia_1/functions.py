import numpy as np
import math


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

    # Edge one is between vertex 1 and 2
    edge1 = {
        "name": "Edge 1",
        "x_min": min(x1, x2),
        "x_max": max(x1, x2),
        "y_min": min(y1, y2),
        "y_max": max(y1, y2),
        "colors": [vcolors[0], vcolors[1]] if y1 < y2 else [vcolors[1], vcolors[0]],
        "down_vertex": [x1, y1] if y1 < y2 else [x2, y2],
        "up_vertex": [x1, y1] if y1 > y2 else [x2, y2],
        # If x2 - x1 is zero set the slope to infinity
        "slope": (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else math.inf,
    }

    # Edge one is between vertex 2 and 3
    edge2 = {
        "name": "Edge 2",
        "x_min": min(x2, x3),
        "x_max": max(x2, x3),
        "y_min": min(y2, y3),
        "y_max": max(y2, y3),
        "colors": [vcolors[1], vcolors[2]] if y2 < y3 else [vcolors[2], vcolors[1]],
        "down_vertex": [x2, y2] if y2 < y3 else [x3, y3],
        "up_vertex": [x2, y2] if y2 > y3 else [x3, y3],
        # If x3 - x2 is zero set the slope to infinity
        "slope": (y3 - y2) / (x3 - x2) if (x3 - x2) != 0 else math.inf,
    }

    # Edge one is between vertex 3 and 1
    edge3 = {
        "name": "Edge 3",
        "x_min": min(x3, x1),
        "x_max": max(x3, x1),
        "y_min": min(y3, y1),
        "y_max": max(y3, y1),
        "colors": [vcolors[2], vcolors[0]] if y3 < y1 else [vcolors[0], vcolors[2]],
        "down_vertex": [x3, y3] if y3 < y1 else [x1, y1],
        "up_vertex": [x3, y3] if y3 > y1 else [x1, y1],
        # If x1 - x1 is zero set the slope to infinity
        "slope": (y1 - y3) / (x1 - x3) if (x1 - x3) != 0 else math.inf,
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

        # Calculate left and right colors for this scanline
        color_left = []
        color_right = []

        # Sort active edges based on x_min:
        sorted_active_edges = sorted(
            active_edges,
            key=lambda x: (x["x_min"], x["x_max"], x["name"]),
        )

        if len(sorted_active_edges) > 1:
            color_left = vector_interp(
                sorted_active_edges[0]["down_vertex"],
                sorted_active_edges[0]["up_vertex"],
                sorted_active_edges[0]["colors"][0],
                sorted_active_edges[0]["colors"][1],
                y,
                2,
            )

            color_right = vector_interp(
                sorted_active_edges[1]["down_vertex"],
                sorted_active_edges[1]["up_vertex"],
                sorted_active_edges[1]["colors"][0],
                sorted_active_edges[1]["colors"][1],
                y,
                2,
            )
        else:
            color_left = color_right = [0, 0, 0]

        # Draw the calculated color for each x in the img
        if len(sorted_active_points) == 1:
            color = vector_interp(
                [sorted_active_points[0][0], y],
                [sorted_active_points[0][0], y],
                color_left,
                color_right,
                sorted_active_points[0][0],
                1,
            )
            img[y, math.floor(sorted_active_points[0][0])] = np.array(color)
        elif len(sorted_active_points) > 1:
            for x in range(
                math.floor(sorted_active_points[0][0]),
                math.floor(sorted_active_points[1][0]),
            ):
                color = vector_interp(
                    [sorted_active_points[0][0], y],
                    [sorted_active_points[1][0], y],
                    color_left,
                    color_right,
                    x,
                    1,
                )
                img[y][x] = color
    return img
