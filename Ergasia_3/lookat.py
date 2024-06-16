import numpy as np


def lookat(
    eye: np.ndarray, up: np.ndarray, target: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    # Calculate the camera's view matrix (i.e., its coordinate frame transformation specified
    # by a rotation matrix R, and a translation vector t).
    # :return a tuple containing the rotation matrix R (3 x 3) and a translation vector
    # t (1 x 3)

    # Flatten all arrays for easier calculations
    eye = eye.flatten()
    up = up.flatten()
    target = target.flatten()

    # Calculate the z of the camera
    z_camera = target - eye
    z_camera_norm = z_camera / np.linalg.norm(z_camera)

    # Calculate the translation vector directly
    t = up - np.dot(up, z_camera_norm) * z_camera_norm

    y_camera_norm = t / np.linalg.norm(t)

    # Find x using the cross product of the other 2 vectors
    x_camera_norm = np.cross(y_camera_norm, z_camera_norm)

    # Save them all in a matrix
    R = np.array([x_camera_norm, y_camera_norm, z_camera_norm])

    # Set the translation vector to be the center of the camera
    translation_vector = eye

    return R, translation_vector
