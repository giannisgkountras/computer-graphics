import numpy as np
from world2view import world2view


def perspective_project(
    pts: np.ndarray, focal: float, R: np.ndarray, t: np.ndarray
) -> tuple[
    np.ndarray, np.ndarray
]:  # Project the specified 3d points pts on the image plane, according to a pinhole perspective projection model.
    pts_camera_world = world2view(pts, R, t)
    projected_points = np.empty((0, 2))
    for point in pts_camera_world:
        projected_x = (np.multiply(focal, point[0])) / point[2]
        projected_y = (np.multiply(focal, point[1])) / point[2]
        projected_point = np.array(
            [[projected_x, projected_y]]
        )  # Create a 2D array for the projected point
        projected_points = np.vstack(
            [projected_points, projected_point]
        )  # Append the projected point array

    return projected_points


# pts = np.array(
#     [[2, 2, 5], [1, 1, 3], [3, 3, 4]]
# )  # Three points: [2, 2, 5], [1, 1, 3], and [3, 3, 4]
# focal = 2  # Focal length
# R = np.eye(3)  # Identity rotation matrix
# t = np.array([0, 0, 1])  # Translation vector
# print(perspective_project(pts, focal, R, t))
