import numpy as np
import matplotlib.pyplot as plt
import re

f = open('file.txt', 'r')
x_list = []
V_list = []

for line in f:
    a_re = re.search(r'(?<=a=\s)[\d\.\de\-]+',line) #s1 = re.search(r'(?<=a=\s)\d+[.]\d+',line)
    b_re = re.search(r'(?<=b=\s)[\d\.\de\-]+',line)
    if a_re:
        x_list.append(float(a_re.group()))
    if b_re:
        V_list.append(float(b_re.group()))

    kif = (re.search(r'(?<=k=\s)[\d\.\de\-]+',line))
    if kif:
        k = float(kif.group())
    dtif = (re.search(r'(?<=dt=\s)[\d\.\de\-]+',line))
    if dtif:
        dt = float(dtif.group())

    t0if = (re.search(r'(?<=t0=\s)[\d\.\de\-]+', line))
    if t0if:
        t0 = float(t0if.group())

#print(x_list)
#print(v_list)
#print(k)
#with open('file.txt', 'r') as f:
#    print(f)
#list = [line.strip() for line in f]
#list = np.loadtxt(f)
#print(re.search('a = ', f_str))

"""
sep = []
for el in list:
    sep.append([float(el.split(" ")[0]),float(el.split(" ")[1])])
Mat = np.array(sep)
#print(Mat)"""

Mat = np.array([x_list, V_list]).T
#print(Mat)

Energy = k*Mat.T[0]**2 / 2 + Mat.T[1]**2 / 2 #np.sqrt((Mat2.T[0] - Mat3.T[0])**2 + (Mat2.T[1] - Mat3.T[1])**2)/dt
print("E_err = E_end/E_0 = ",Energy[-1] / Energy[0])

#x_list = Mat.T[0]
#V_list = Mat.T[1]

fig, gr = plt.subplots(1,4)
gr[0].plot(Mat.T[0], Mat.T[1])
gr[0].set_xlabel('?????a???')
gr[0].set_ylabel('?????b???')
#gr[0].xlabel("a")
#gr[0].ylabel("b")
gr[1].plot(Energy)
gr[1].set_xlabel('step')
gr[1].set_ylabel('E')

gr[2].plot(x_list)
gr[2].set_xlabel('step')
gr[2].set_ylabel('x')

gr[3].plot(V_list)
gr[3].set_xlabel('step')
gr[3].set_ylabel('y')
plt.show()

delta_E = Energy[-1] - Energy[0]
f_dE_dt = open('dE_dt.txt', 'a')
#print(delta_E, " ", dt, " ")
print("delta_E= ", delta_E, " ", "dt= ", dt, " ", "t0= ", t0, file=f_dE_dt)
f_dE_dt.close()
