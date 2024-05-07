import numpy as np


def lookat(
    eye: np.ndarray, up: np.ndarray, target: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    # Calculate the camera's view matrix (i.e., its coordinate frame transformation specified
    # by a rotation matrix R, and a translation vector t).
    # :return a tuple containing the rotation matrix R (3 x 3) and a translation vector
    # t (1 x 3)
    eye = eye.flatten()
    up = up.flatten()
    target = target.flatten()

    z_camera = target - eye
    z_camera_norm = z_camera / np.linalg.norm(z_camera)

    # Calculate the translation vector directly
    t = up - np.dot(up, z_camera_norm) * z_camera_norm

    y_camera_norm = t / np.linalg.norm(t)

    x_camera_norm = np.cross(y_camera_norm, z_camera_norm)

    R = np.array([x_camera_norm, y_camera_norm, z_camera_norm]).T

    translation_vector = eye

    return R, translation_vector


# eye = np.array([15, 15, 1.5])
# up = np.array([0, 0, 1])
# target = np.array([30, 30, 4])

# R, t = lookat(eye, up, target)
# print("Rotation matrix R:")
# print(R)
# print("Translation vector t:")
# print(t)
