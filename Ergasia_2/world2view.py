import numpy as np


def world2view(pts: np.ndarray, R: np.ndarray, c0: np.ndarray) -> np.ndarray:
    # Implements a world-to-view transform, i.e. transforms the specified
    # points to the coordinate frame of a camera. The camera coordinate frame
    # is specified rotation (w.r.t. the world frame) and its point of reference
    # (w.r.t. to the world frame)

    # Initialise empty array for the transformed points
    transformed_pts = []

    # Transform all points (use transpose in order to acces points one by one)
    for point in pts.T:
        # Rotate the point
        transformed_point = np.dot(R.T, point)

        # Transpose the point
        transformed_point = transformed_point + c0

        # Append updated point to the array
        transformed_pts.append(transformed_point)

    return np.array(transformed_pts)
