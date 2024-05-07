import numpy as np


def world2view(pts: np.ndarray, R: np.ndarray, c0: np.ndarray) -> np.ndarray:
    # Implements a world-to-view transform, i.e. transforms the specified
    # points to the coordinate frame of a camera. The camera coordinate frame
    # is specified rotation (w.r.t. the world frame) and its point of reference
    # (w.r.t. to the world frame)

    pts = pts.T
    transformed_pts = []

    for point in pts:
        transformed_point = np.dot(R.T, point)
        transformed_point = transformed_point + c0
        transformed_pts.append(transformed_point)

    return np.array(transformed_pts)


# pts = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # Three points
# R = np.eye(3)  # Identity rotation matrix (no rotation)
# c0 = np.array([0, 0, 0])  # Camera at the origin

# # Call the world2view function
# result = world2view(pts, R, c0)

# print(result)
