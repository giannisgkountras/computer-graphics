import numpy as np


def lookat(
    eye: np.ndarray, up: np.ndarray, target: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    # Calculate the camera's view matrix (i.e., its coordinate frame transformation specified
    # by a rotation matrix R, and a translation vector t).
    # :return a tuple containing the rotation matrix R (3 x 3) and a translation vector
    # t (1 x 3)

    z_camera = target - eye
    z_camera_norm = z_camera / np.linalg.norm(z_camera)

    t = up - np.dot(up, z_camera_norm) * z_camera_norm

    y_camera_norm = t / np.linalg.norm(t)

    x_camera_norm = np.cross(z_camera_norm, y_camera_norm)

    R = np.array([x_camera_norm, y_camera_norm, z_camera_norm])

    translation_vector = eye

    return R, translation_vector


# eye = np.array([0, 0, 1])
# up = np.array([0, 1, 0])
# target = np.array([1, 1, 1])

# R, t = lookat(eye, up, target)
# print("Rotation matrix R:")
# print(R)
# print("Translation vector t:")
# print(t)
