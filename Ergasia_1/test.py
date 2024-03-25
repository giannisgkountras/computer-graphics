import numpy as np
from vector_interp import vector_interp

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

data = np.load('hw1.npy')
print(data)
np.load = np_load_old