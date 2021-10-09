import numpy as np
#import random

x_list = np.arange(0,10,0.1)
a = 4
b = 2
err_size = 0.5

err_list = (np.random.sample(x_list.size) * 2 - 1) * err_size
y_list = a * x_list + b + err_list

#points = np.column_stack([x_list, y_list])#np.vstack((x_list, y_list)).transpose()#np.column_stack([x_list, y_list])
A = np.column_stack([x_list, np.ones(len(x_list))])
a_calc, b_calc = np.linalg.lstsq(A, y_list, rcond=None)[0]
#np.linalg.lstsq(points)
#help(np.linalg.lstsq)
print(a_calc, b_calc)