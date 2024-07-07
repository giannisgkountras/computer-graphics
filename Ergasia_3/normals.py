import numpy as np


def calculate_normals(verts, faces):

    normals = np.zeros(shape=verts.shape)

    # Initialize normals for each vertex to zero
    # Iterate over each face to compute face normals
    for face in faces:
        # Get the vertices number from the face
        idx1, idx2, idx3 = face

        # Vertices of the triangle
        v1 = verts[idx1]
        v2 = verts[idx2]
        v3 = verts[idx3]
        # Compute the vectors from the vertices of the triangle
        vec1 = v2 - v1
        vec2 = v3 - v1

        # Compute the normal of the triangle using the cross product
        face_normal = np.cross(vec1, vec2)

        # Normalize the face normal
        face_normal = face_normal / np.linalg.norm(face_normal)

        # Add the face normal to each of the triangle's vertices' normals
        normals[idx1] += face_normal
        normals[idx2] += face_normal
        normals[idx3] += face_normal

    # Normalize the accumulated normals for each vertex, skipping zero normals
    normals = [
        normal / np.linalg.norm(normal) if np.linalg.norm(normal) != 0 else normal
        for normal in normals
    ]
    return np.array(normals)
