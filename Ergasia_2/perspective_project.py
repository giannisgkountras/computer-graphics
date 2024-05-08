import numpy as np
from world2view import world2view


def perspective_project(
    pts: np.ndarray, focal: float, R: np.ndarray, t: np.ndarray
) -> tuple[
    np.ndarray, np.ndarray
]:  # Project the specified 3d points pts on the image plane, according to a pinhole perspective projection model.

    # Transform the points to the camera system
    pts_camera_world = world2view(pts, R, t)

    # Save the depths of the points
    z_values = [sub_array[2] for sub_array in pts_camera_world]

    # Project all points on the camera
    projected_points = np.empty((0, 2))
    for point in pts_camera_world:
        projected_x = np.multiply(focal / point[2], point[0])
        projected_y = np.multiply(focal / point[2], point[1])
        projected_point = np.array(
            [[projected_x, projected_y]]
        )  # Create a 2D array for the projected point
        projected_points = np.vstack(
            [projected_points, projected_point]
        )  # Append the projected point array

    return projected_points, z_values
