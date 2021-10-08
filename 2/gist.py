import matplotlib.pyplot as plt
import numpy as np

phase = 1
d_angle = 0.000001*2*np.pi
number_figur = 2

fig, gr = plt.subplots(number_figur,2)
list_angle = np.arange(0, 2*np.pi*number_figur, d_angle)

for i in range(number_figur):
    list_y = np.sin((list_angle + phase))
    list_x = np.sin(list_angle*(i+1))
    gr[i][0].hist(list_x, bins=30)
    gr[i][1].hist(list_y, bins=30)

plt.show()