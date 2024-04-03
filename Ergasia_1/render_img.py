import numpy as np
from f_shading import f_shading
from g_shading import g_shading
from f_shading_2 import f_shading_2
from g_shading_2 import g_shading_2


def render_img(faces, vertices, vcolors, depth, shading):
    """
        Function to render the image from multiple triangles

        Args:
        faces (Kx3 array): Array of triangles, each row contains the vertices of a triangle by references the vertices array
        vertices (Lx2 array): Array of coordinates of vertices
        vcolors (Lx3 array): Each row contains the color of the corresponding vertex in RGB [0,1]
        depth (Lx1 array): Each row contains the depth of the corresponding vertex before the 2D projection
        shading (string): The shading function to be used, "f" means Flat and "g" means Gouraud

    Returns
        MxNx3 array filled with colored triangles:
    """
    # Initialise the image as a 512 by 512 array with white color
    img = np.ones((512, 512, 3), dtype=float)

    print("Loading...")
    triangles = []
    for face in faces:
        # Calculate triangle depth
        vertices_depth = [depth[face[0]], depth[face[1]], depth[face[2]]]
        triangle_depth = (vertices_depth[0] + vertices_depth[1] + vertices_depth[2]) / 3

        # Initialise all triangles
        triangle = {
            "vertices": [vertices[face[0]], vertices[face[1]], vertices[face[2]]],
            "color": [vcolors[face[0]], vcolors[face[1]], vcolors[face[2]]],
            "depth": triangle_depth,
        }

        # Keep all triangles in an array
        triangles.append(triangle)

    # Sort the array of triangles based on depth (far first)
    triangles_sorted = sorted(triangles, key=lambda x: x["depth"], reverse=True)

    # Render the image based on the shading method
    if shading == "f":
        for triangle in triangles_sorted:
            img = f_shading_2(img, triangle["vertices"], triangle["color"])
    elif shading == "g":
        for triangle in triangles_sorted:
            img = g_shading_2(img, triangle["vertices"], triangle["color"])
    else:
        print("Invalid shading option")

    return img
