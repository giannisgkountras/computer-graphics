import numpy as np


def rasterize(
    pts_2d: np.ndarray, plane_w: int, plane_h: int, res_w: int, res_h: int
) -> np.ndarray:
    # Rasterize the incoming 2d points from the camera plane to image pixel coordinates

    for point in pts_2d:
        x_actual = point[0] + plane_w / 2
        print(x_actual)
        y_actual = point[1] + plane_h / 2
        scale_x = x_actual / plane_w
        print(scale_x)
        scale_y = y_actual / plane_h
        point[0] = np.round(scale_x * res_w)
        point[1] = np.round(scale_y * res_h)

    return pts_2d


# pts = [[-0.5, 0.5]]
# print(rasterize(pts, 1, 1, 100, 100))
