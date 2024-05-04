import numpy as np


def rasterize(
    pts_2d: np.ndarray, plane_w: int, plane_h: int, res_w: int, res_h: int
) -> np.ndarray:
    # Rasterize the incoming 2d points from the camera plane to image pixel coordinates

    scale_x = res_w / plane_w
    scale_y = res_h / plane_h
    mapped_pts = pts_2d * np.array([scale_x, scale_y])
    pixel_coords = np.round(mapped_pts).astype(int)
    # Ensure pixel coordinates are within image bounds
    pixel_coords[:, 0] = np.clip(pixel_coords[:, 0], 0, res_w - 1)
    pixel_coords[:, 1] = np.clip(pixel_coords[:, 1], 0, res_h - 1)

    # for point in pts_2d:
    #     print("===============")
    #     print("Point is ", point)
    #     x_actual = point[0] + plane_w / 2
    #     y_actual = point[1] + plane_h / 2
    #     print("x and y actual are ", x_actual, y_actual)
    #     scale_x = x_actual / plane_w
    #     scale_y = y_actual / plane_h
    #     point[0] = np.round(scale_x * res_w)
    #     point[1] = np.round(scale_y * res_h)
    #     print("Final point is ", point)
    #     print("===============")

    return pixel_coords


# pts = [[-0.5, 0.5]]
# print(rasterize(pts, 1, 1, 100, 100))
