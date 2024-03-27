import numpy as np
from functions import vector_interp
from functions import f_shading
import cv2

np_load_old = np.load
np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
data = np.load("hw1.npy")
# print(data)
# np.load = np_load_old
img = np.zeros((512, 512, 3), dtype=np.uint8)
# p1 = [0, 10]
# p2 = [10, 0]
# V1 = [0, 0, 0]
# V2 = [2, 2, 2]
# coord = 0
# dim = 1

# print(vector_interp(p1, p2, V1, V2, coord, dim))

updated_img = f_shading(
    img,
    [
        [100, 40],
        [413, 500],
        [300, 40],
    ],
    [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
)
updated_img[:, :, 0] = updated_img[:, :, 0] * 255
updated_img[:, :, 1] = updated_img[:, :, 1] * 255
updated_img[:, :, 2] = updated_img[:, :, 2] * 255

# image_bgr = cv2.cvtColor(updated_img, cv2.COLOR_RGB2BGR)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
