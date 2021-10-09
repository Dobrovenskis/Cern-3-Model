import numpy as np
import matplotlib.pyplot as plt

f = open('file.txt', 'r')
list = [line.strip() for line in f]

k = float(list[0][4:])
#print(list[0][4::])
list.pop(0)

sep = []
for el in list:
    sep.append([float(el.split(" ")[0]),float(el.split(" ")[1])])
Mat = np.array(sep)
#print(Mat)

Energy = k*Mat.T[0]**2 / 2 + Mat.T[1]**2 / 2 #np.sqrt((Mat2.T[0] - Mat3.T[0])**2 + (Mat2.T[1] - Mat3.T[1])**2)/dt
print("E_err = E_end/E_0 = ",Energy[-1] / Energy[0])

x_list = Mat.T[0]
V_list = Mat.T[1]

fig, gr = plt.subplots(1,4)
gr[0].plot(Mat.T[0], Mat.T[1])
gr[0].set_xlabel('?????a???')
gr[0].set_ylabel('?????b???')
#gr[0].xlabel("a")
#gr[0].ylabel("b")
gr[1].plot(Energy)
gr[0].set_xlabel('step')
gr[0].set_ylabel('E')

gr[2].plot(x_list)

gr[3].plot(V_list)
plt.show()


