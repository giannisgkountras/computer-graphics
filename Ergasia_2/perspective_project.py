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

    # Initialise empty array for projected points
    projected_points = []

    # Calculate x and y for all points
    for point in pts_camera_world:
        projected_x = np.multiply(focal / point[2], point[0])
        projected_y = np.multiply(focal / point[2], point[1])

        # Append the projected point array
        projected_points.append([projected_x, projected_y])

    # Make projected points a numpy array
    projected_points = np.array(projected_points)

    return projected_points, z_values
