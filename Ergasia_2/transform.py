import numpy as np

identity = np.eye(4)
# |1 0 0 0|
# |0 1 0 0|
# |0 0 1 0|
# |0 0 0 1|


# Interface for performing affine transformations.
class Transform:
    # Initialize a Transform object.
    def __init__(self):
        self.mat = identity

    # rotate the transformation matrix
    def rotate(self, theta: float, u: np.ndarray) -> None:
        ux = u[0]
        uy = u[1]
        uz = u[2]
        R = (
            (1 - np.cos(theta))
            * np.array(
                [
                    [ux**2, ux * uy, ux * uz],
                    [ux * uy, uy**2, uy * uz],
                    [uz * ux, uz * uy, uz**2],
                ]
            )
            + np.cos(theta) * np.eye(3)
            + np.sin(theta) * np.array([[0, -uz, uy], [uz, 0, -ux], [-uy, ux, 0]])
        )
        # R_h = [[R, np.zeros((3, 1))], [np.zeros((1, 3)), 1]]
        R_h = np.block([[R, np.zeros((3, 1))], [np.zeros((1, 3)), 1]])

        self.mat = R_h

    # translate the transformation matrix.
    def translate(self, t: np.ndarray) -> None:
        # Make the t vector homogeneous
        t_homogeneous = np.append(t, 0)
        self.mat[:, -1] = t_homogeneous

    # transform the specified points
    # according to our current matrix.
    def transform_pts(self, pts: np.ndarray) -> np.ndarray:
        for i, point in enumerate(pts):
            point_h = np.append(point, 1)
            updated_point_h = np.dot(self.mat, point_h)
            pts[i] = np.delete(updated_point_h, -1)

        return pts
