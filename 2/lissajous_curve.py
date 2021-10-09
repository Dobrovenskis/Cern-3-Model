import matplotlib.pyplot as plt
import numpy as np

phase = 1
d_angle = 0.000001*2*np.pi
number_figur = 2
kx = [2, 1]
ky = [2, 3]

fig, gr = plt.subplots(number_figur)
list_angle = np.arange(0, 2*np.pi*number_figur, d_angle)


for i in range(number_figur):
    list_y = np.sin((list_angle + phase)*ky[i])
    list_x = np.sin(list_angle * (i + 1)*kx[i])
    gr[i].plot(list_y, list_x)

plt.show()