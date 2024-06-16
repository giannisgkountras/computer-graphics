import numpy as np
from normals import calculate_normals
from perspective_project import perspective_project
from lookat import lookat
from rasterize import rasterize
from shade_gouraud import shade_gouraud


def render_object(
    shader,
    focal,
    eye,
    lookat_target,
    up,
    bg_color,
    M,
    N,
    H,
    W,
    verts,
    vert_colors,
    faces,
    ka,
    kd,
    ks,
    n,
    lpos,
    lint,
    lamb,
):
    vert_colors = vert_colors.T
    verts = verts.T
    faces = faces.T

    img = np.ones((M, N, 3), dtype=float)

    normals = calculate_normals(verts, faces)

    R_c, t_c = lookat(eye, up, lookat_target)

    projected_points, z_values = perspective_project(verts.T, focal, R_c, t_c)

    points_2d = rasterize(projected_points, W, H, M, N)

    print("Rendering...")

    triangles = []
    for face in faces:
        # Calculate triangle depth
        vertices_depth = [z_values[face[0]], z_values[face[1]], z_values[face[2]]]
        triangle_depth = (vertices_depth[0] + vertices_depth[1] + vertices_depth[2]) / 3
        vertsp = [
            verts[face[0]],
            verts[face[1]],
            verts[face[2]],
        ]
        vertsn = [normals[face[0]], normals[face[1]], normals[face[2]]]
        vertsc = [vert_colors[face[0]], vert_colors[face[1]], vert_colors[face[2]]]
        bcoords = (verts[face[0]] + verts[face[1]] + verts[face[2]]) / 3
        cam_pos = eye
        verts_2d = [points_2d[face[0]], points_2d[face[1]], points_2d[face[2]]]
        # Initialise all triangles
        triangle = {
            "vertices": vertsp,
            "normals": vertsn,
            "color": vertsc,
            "depth": triangle_depth,
            "points_2d": verts_2d,
            "bcoords": bcoords,
        }

        # Keep all triangles in an array
        triangles.append(triangle)

    # Sort the array of triangles based on depth (far first)
    triangles_sorted = sorted(triangles, key=lambda x: x["depth"], reverse=True)

    # Render the image based on the shading method
    if shader == "gouraud":
        for triangle in triangles_sorted:
            img = shade_gouraud(
                triangle["vertices"],
                triangle["normals"],
                triangle["color"],
                triangle["bcoords"],
                cam_pos,
                ka,
                kd,
                ks,
                n,
                lpos,
                lint,
                lamb,
                img,
                triangle["points_2d"],
            )

    return img
