import numpy as np
from functions import vector_interp

# np_load_old = np.load
# np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
# data = np.load('hw1.npy')
# print(data)
# np.load = np_load_old

p1 = [0, 10]
p2 = [0, 0]
V1 = [0, 0, 0]
V2 = [2, 2, 2]
coord = 0
dim = 2

print(vector_interp(p1, p2, V1, V2, coord, dim))
