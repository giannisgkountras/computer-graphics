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
        # Reverse theta in order to perform right rotation
        theta = -theta

        # Initialise ux uy and uz from u
        ux = u[0]
        uy = u[1]
        uz = u[2]

        # Calculate R based on the notes
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

        # Make R homogeneous
        R_h = np.block([[R, np.zeros((3, 1))], [np.zeros((1, 3)), 1]])

        # Update self.mat
        self.mat = np.dot(R_h, self.mat)

    # translate the transformation matrix.
    def translate(self, t: np.ndarray) -> None:
        # Make the t vector homogeneous
        T = np.eye(4)
        T[:3, 3] = t

        # Update self.mat
        self.mat = np.dot(T, self.mat)

    def transform_pts(self, pts: np.ndarray) -> np.ndarray:
        # Initialise empty array for transformed points
        transformed_pts = []

        # Transform all points (use transposed points in order to access them one by one)
        for point in pts.T:
            # Make each point homogeneous
            point_h = np.append(point, 1)

            # Update point using self.mat
            updated_point_h = np.dot(self.mat, point_h)

            # Revert point to non homogenous
            updated_point_h = np.delete(updated_point_h, -1)

            # Add updated point to transformed points array
            transformed_pts.append(updated_point_h)

        # Return the transposed transform points in order to revert them to their original structure
        return np.array(transformed_pts).T
