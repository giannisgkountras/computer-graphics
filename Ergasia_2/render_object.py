import numpy as np
from lookat import lookat
from perspective_project import perspective_project
from rasterize import rasterize
from render_img import render_img


def render_object(
    v_pos, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target
) -> np.ndarray:
    # render the specified object from the specified camera

    # Transform camera details to R and t vectors
    R_c, t_c = lookat(eye, up, target)

    # Transform points to camera system and project them
    points_camera_world, depth = perspective_project(v_pos, focal, R_c, t_c)

    # Rasterise the points in order to be used in the image
    points_2d = rasterize(points_camera_world, plane_w, plane_h, res_w, res_h)

    # Render the image using the function from the previous project
    img = render_img(t_pos_idx, points_2d, v_clr, depth, "g")

    return img
