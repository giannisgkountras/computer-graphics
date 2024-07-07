from light import light
from vector_interp import vector_interp, normal_interp
from bilerp import bilerp


def shade_phong(
    vertsp,
    vertsn,
    vertsc,
    bcoords,
    cam_pos,
    ka,
    kd,
    ks,
    n,
    lpos,
    lint,
    lamb,
    X,
    points_2d,
    uvs,
    texture_map,
):
    # Color no longer needed since we use texture map
    # They are left in the code for testing without the texture map
    colors = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    img = X
    vertices = points_2d
    vcolors = colors
    # CHANGE g_shading.py IN ORDER TO IMPLEMENT PHONG SHADING

    # Save coordinates of each vertex
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
        "top_color": vcolors[0] if y1 > y2 else vcolors[1],
        "bottom_color": vcolors[1] if y1 > y2 else vcolors[0],
        # ADDED NORMAL VECTORS INFORMATION
        "top_normal": vertsn[0] if y1 > y2 else vertsn[1],
        "bottom_normal": vertsn[1] if y1 > y2 else vertsn[0],
        # ADDED UV VECTORS INFORMATION
        "top_uv": uvs[0] if y1 > y2 else uvs[1],
        "bottom_uv": uvs[1] if y1 > y2 else uvs[0],
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
        # ADDED NORMAL VECTORS INFORMATION
        "top_normal": vertsn[1] if y2 > y3 else vertsn[2],
        "bottom_normal": vertsn[2] if y2 > y3 else vertsn[1],
        # ADDED UV VECTORS INFORMATION
        "top_uv": uvs[1] if y1 > y2 else uvs[2],
        "bottom_uv": uvs[2] if y1 > y2 else uvs[1],
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
        # ADDED NORMAL VECTORS INFORMATION
        "top_normal": vertsn[2] if y3 > y1 else vertsn[0],
        "bottom_normal": vertsn[0] if y3 > y1 else vertsn[2],
        # ADDED UV VECTORS INFORMATION
        "top_uv": uvs[2] if y1 > y2 else uvs[0],
        "bottom_uv": uvs[0] if y1 > y2 else uvs[2],
    }

    edges = [edge1, edge2, edge3]

    # Calculate the y_min and y_max of the triangle
    y_min_total = min(y1, y2, y3)
    y_max_total = max(y1, y2, y3)

    # Initialise active edges as empty array
    active_edges = []

    # Initialise an array that stores active points and their correspoding color
    # This array will look like this: [[[x1,y1],[R,G,B]], [[x2,y2],[R,G,B]]]
    active_points_colors = []

    for y in range(y_min_total, y_max_total + 1):
        for edge in edges:

            # Append new active edges if they are not horizontal
            if edge["y_min"] == y and edge["y_max"] != edge["y_min"]:
                active_edges.append(edge)

            # Remove no longer active edges
            elif edge["y_max"] == y and edge in active_edges:
                active_edges.remove(edge)

        # Reset active points colors for given y
        active_points_colors = []

        # Calculate active points using the slope of the edge and current y
        # plus their color based on the edges colors with interpolation
        for active_edge in active_edges:
            # The color is calculated between the vectors of the edge and current y
            # No longer needed because of texture map

            color = [0, 0, 0]
            # color = vector_interp(
            #     [
            #         0,  # We calculate based on y, so we give x any value, we don't care
            #         active_edge["y_min"],
            #     ],
            #     [
            #         0,  # We calculate based on y, so we give x any value, we don't care
            #         active_edge["y_max"],
            #     ],
            #     active_edge["bottom_color"],
            #     active_edge["top_color"],
            #     y,
            #     2,
            # )

            # INTERPOLATE FOR THE NORMAL TOO
            normal = normal_interp(
                [
                    0,  # We calculate based on y, so we give x any value, we don't care
                    active_edge["y_min"],
                ],
                [
                    0,  # We calculate based on y, so we give x any value, we don't care
                    active_edge["y_max"],
                ],
                active_edge["bottom_normal"],
                active_edge["top_normal"],
                y,
                2,
            )

            uv = vector_interp(
                [
                    0,  # We calculate based on y, so we give x any value, we don't care
                    active_edge["y_min"],
                ],
                [
                    0,  # We calculate based on y, so we give x any value, we don't care
                    active_edge["y_max"],
                ],
                active_edge["bottom_uv"],
                active_edge["top_uv"],
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
                        normal,
                        uv,
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
                        normal,
                        uv,
                    ]
                )

            # When slope == 0 we add no active points because the points of the horizontal
            # edge are already calculated in the other 2 edges that contain them.
            elif active_edge["slope"] == 0 and y == y_min_total:
                pass

            elif active_edge["slope"] == float("inf"):
                active_points_colors.append(
                    [[active_edge["x_min"], y], color, normal, uv]
                )

        # Sort active points from leftest to rightest
        active_points_colors = sorted(active_points_colors, key=lambda x: x[0][0])

        # Draw on the image for all intermediate points
        if len(active_points_colors) == 2:
            # active_points_colors looks like this [[[x1,y1],[R,G,B], [Nx, Ny, Nz]], [[x2,y2],[R,G,B] , [Nx, Ny, Nz]]]
            # so [0][0][0] is x1 and [1][0][0] is x2
            for x in range(
                round(active_points_colors[0][0][0]),
                round(active_points_colors[1][0][0]),
            ):
                # No longer needed because of texture map
                # color = vector_interp(
                #     [
                #         active_points_colors[0][0][0],  # This is x1
                #         0,  # We calculate based on x, so we give y any value, we don't care
                #     ],
                #     [
                #         active_points_colors[1][0][0],  # This is x2
                #         0,  # We calculate based on x, so we give y any value, we don't care
                #     ],
                #     active_points_colors[0][
                #         1
                #     ],  # This is the color of the left active point
                #     active_points_colors[1][
                #         1
                #     ],  # This is the color of the right active point
                #     x,
                #     1,
                # )

                normal = normal_interp(
                    [
                        active_points_colors[0][0][0],  # This is x1
                        0,  # We calculate based on x, so we give y any value, we don't care
                    ],
                    [
                        active_points_colors[1][0][0],  # This is x2
                        0,  # We calculate based on x, so we give y any value, we don't care
                    ],
                    active_points_colors[0][
                        2
                    ],  # This is the normal of the left active point
                    active_points_colors[1][
                        2
                    ],  # This is the normal of the right active point
                    x,
                    1,
                )

                uv = vector_interp(
                    [
                        active_points_colors[0][0][0],  # This is x1
                        0,  # We calculate based on x, so we give y any value, we don't care
                    ],
                    [
                        active_points_colors[1][0][0],  # This is x2
                        0,  # We calculate based on x, so we give y any value, we don't care
                    ],
                    active_points_colors[0][
                        3
                    ],  # This is the uv of the left active point
                    active_points_colors[1][
                        3
                    ],  # This is the uv of the right active point
                    x,
                    1,
                )
                texture_color = bilerp(uv, texture_map)

                I = light(
                    bcoords,
                    normal,
                    texture_color,
                    cam_pos,
                    ka,
                    kd,
                    ks,
                    n,
                    lpos,
                    lint,
                    lamb,
                )

                img[y][x] = I

    return img
