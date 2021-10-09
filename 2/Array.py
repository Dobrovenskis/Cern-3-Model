import numpy as np

size = 10
B = 2*np.eye(size)
B -= np.diag(np.ones([size - 1], dtype = np.int), 1)
B -= np.diag(np.ones([size - 1], dtype = np.int), -1)

print(B)