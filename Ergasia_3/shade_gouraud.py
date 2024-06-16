from g_shading import g_shading
from light import light
from rasterize import rasterize


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
):

    colors = []

    for i, point in enumerate(vertsp):

        I = light(point, vertsn[i], vertsc[i], cam_pos, ka, kd, ks, n, lpos, lint, lamb)
        colors.append(I)

    X = g_shading(X, points_2d, colors)

    return X
