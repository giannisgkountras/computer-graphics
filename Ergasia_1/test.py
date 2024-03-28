import numpy as np
import cv2
import math
from functions import vector_interp
from functions import f_shading
from functions import g_shading

# np_load_old = np.load
# np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
# data = np.load("hw1.npy")
# print(data)
# np.load = np_load_old

img = np.ones((512, 512, 3), dtype=float)

# updated_img = f_shading(
#     img,
#     [
#         [100, 40],
#         [413, 500],
#         [300, 40],
#     ],
#     [[1.0, 0.4, 0.2], [0.1, 0, 0.9], [0.0, 0.0, 1.0]],
# )


g_img = g_shading(
    img,
    [[20, 20], [300, 70], [400, 400]],
    [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
)

# updated_img *= 255
# updated_img = updated_img.astype(np.uint8)
g_img *= 255
g_img = g_img.astype(np.uint8)
rgb_g_img = cv2.cvtColor(g_img, cv2.COLOR_BGR2RGB)

cv2.imshow("Image", rgb_g_img)
# cv2.imshow("Image", updated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
