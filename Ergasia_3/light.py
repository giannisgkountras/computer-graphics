import numpy as np


def light(point, normal, vcolor, cam_pos, ka, kd, ks, n, lpos, lint, lamb):

    # View vector (from point to camera)
    view_vector = cam_pos - point
    view_vector = view_vector / np.linalg.norm(view_vector)

    # Ambient component
    ambient = ka * lamb

    # Initialize the final color with the ambient component
    I = np.zeros(3)
    I += ambient

    # Process each light source
    for i in range(np.array(lpos).shape[0]):
        # Light position and intensity
        light_pos = lpos[i]
        light_intensity = lint[i]

        # Light vector (from point to light source)
        light_vector = light_pos - point
        light_vector = light_vector / np.linalg.norm(light_vector)

        # Diffuse component
        diff = max(np.dot(normal, light_vector), 0)
        diffuse = kd * diff * vcolor * light_intensity

        # Reflect vector (for specular component)
        reflect_vector = 2 * np.dot(normal, light_vector) * normal - light_vector
        reflect_vector = reflect_vector / np.linalg.norm(reflect_vector)

        # Specular component
        spec = max(np.dot(view_vector, reflect_vector), 0)
        specular = ks * (spec**n) * light_intensity

        # Add the contributions of this light source
        I += diffuse + specular

    # Ensure the final intensity is within the range [0, 1]
    I = np.clip(I, 0, 1)

    return I


# Example usage
# point = np.array([1, 2, 3])
# normal = np.array([0, 0, 1])
# vcolor = np.array([0.5, 0.5, 0.5])
# cam_pos = np.array([0, 0, 10])
# ka = 0.1
# kd = 0.7
# ks = 0.5
# n = 10
# lpos = np.array([[10, 10, 10], [20, 20, 20]])
# lint = np.array([[1, 1, 1], [0.5, 0.5, 0.5]])

# I = light(point, normal, vcolor, cam_pos, ka, kd, ks, n, lpos, lint)
# print("Resulting color intensity:", I)
