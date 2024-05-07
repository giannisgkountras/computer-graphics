import numpy as np


def rasterize(
    pts_2d: np.ndarray, plane_w: int, plane_h: int, res_w: int, res_h: int
) -> np.ndarray:
    # Rasterize the incoming 2d points from the camera plane to image pixel coordinates

    scale_x = res_w / plane_w
    scale_y = res_h / plane_h

    mapped_pts = []
    for point in pts_2d:
        mapped_x = point[0] + plane_w / 2
        mapped_y = point[1] + plane_h / 2
        mapped_x = mapped_x * scale_x
        mapped_y = mapped_y * scale_y
        mapped_pts.append([mapped_x, mapped_y])

    pixel_coords = np.round(mapped_pts).astype(int)
    return pixel_coords
