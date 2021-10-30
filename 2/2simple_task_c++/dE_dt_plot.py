import matplotlib.pyplot as plt
import re

f = open('dE_dt.txt', 'r')
E_list = []
dt_list = []

for line in f:
    E_re = re.search(r'(?<=delta_E=\s\s)[\d\.\de\-]+',line) #s1 = re.search(r'(?<=a=\s)\d+[.]\d+',line)
    dt_re = re.search(r'(?<=dt=\s\s)[\d\.\de\-]+',line)
    if E_re:
        E_list.append(float(E_re.group()))
    if dt_re:
        dt_list.append(float(dt_re.group()))
#print(E_list)
plt.scatter(dt_list, E_list)
plt.show()