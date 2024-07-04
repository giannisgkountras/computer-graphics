from g_shading import g_shading
from light import light
from bilerp import bilerp


def shade_gouraud(
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

    colors = []

    texture_colors = [bilerp(uv, texture_map) for uv in uvs]

    for i in range(len(vertsp)):

        I = light(
            bcoords,
            vertsn[i],
            texture_colors[i],
            cam_pos,
            ka,
            kd,
            ks,
            n,
            lpos,
            lint,
            lamb,
        )
        colors.append(I)

    X = g_shading(X, points_2d, colors)

    return X
