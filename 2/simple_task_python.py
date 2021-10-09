import numpy as np
import matplotlib.pyplot as plt
import time


size = 1000000
R = 5
dt = 0.001
k = 1

Mat = np.zeros(shape = (size, 2), dtype=float)
Mat[0][0] = R
Mat[0][1] = 0.0

start_time = time.perf_counter()

for i in range(size - 1):
    Mat[i + 1][0] = Mat[i][0] + Mat[i][1] * dt
    Mat[i + 1][1] = Mat[i][1] - Mat[i][0] * k * dt

print(time.perf_counter() - start_time)

start_time = time.perf_counter()

#Mat2 = np.delete(Mat, -1, 0)
#Mat3 = np.delete(Mat, 0, 0)
Energy = k*Mat.T[0]**2 / 2 + Mat.T[1]**2 / 2 #np.sqrt((Mat2.T[0] - Mat3.T[0])**2 + (Mat2.T[1] - Mat3.T[1])**2)/dt
print("E_err = E_end/E_0 = ",Energy[-1] / Energy[0])
print(time.perf_counter() - start_time)

fig, gr = plt.subplots(1,2)
gr[0].plot(Mat.T[0], Mat.T[1])
gr[1].plot(Energy)
plt.show()