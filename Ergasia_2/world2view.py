import numpy as np


def world2view(pts: np.ndarray, R: np.ndarray, c0: np.ndarray) -> np.ndarray:
    # Implements a world-to-view transform, i.e. transforms the specified
    # points to the coordinate frame of a camera. The camera coordinate frame
    # is specified rotation (w.r.t. the world frame) and its point of reference
    # (w.r.t. to the world frame)

    # R_h = np.block([[R.T, np.dot(-R.T, c0)], [np.zeros((1, 3)), 1]])
    # pts_homogeneous = np.hstack((pts, np.ones((len(pts), 1))))
    # transformed_pts = np.dot(R_h, pts_homogeneous)
    # return transformed_pts

    transformed_pts = np.dot(R, pts.T).T

    # Translate points by subtracting camera's point of reference
    translated_pts = transformed_pts - c0

    return translated_pts


pts = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # Three points
R = np.eye(3)  # Identity rotation matrix (no rotation)
c0 = np.array([0, 0, 0])  # Camera at the origin

# Call the world2view function
result = world2view(pts, R, c0)

print(result)
