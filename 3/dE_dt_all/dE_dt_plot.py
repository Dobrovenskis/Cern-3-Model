import matplotlib.pyplot as plt
import re

f_kox = open('C:/Users/1/C++/Model/3/Kox_sum/dE_dt.txt', 'r')
E_kox_list = []
dt_kox_list = []

for line in f_kox:
    E_re = re.search(r'(?<=delta_E=\s\s)[\d\.\de\-]+',line) #s1 = re.search(r'(?<=a=\s)\d+[.]\d+',line)
    dt_re = re.search(r'(?<=dt=\s\s)[\d\.\de\-]+',line)
    if E_re:
        E_kox_list.append(float(E_re.group()))
    if dt_re:
        dt_kox_list.append(float(dt_re.group()))
#print(dt_kox_list)
plt.scatter(dt_kox_list, E_kox_list, color="green")

f_predkor = open('C:/Users/1/C++/Model/2/2simple_task_c++/dE_dt.txt', 'r')
E_predkor_list = []
dt_predkor_list = []

for line in f_predkor:
    E_re = re.search(r'(?<=delta_E=\s\s)[\d\.\de\-]+',line) #s1 = re.search(r'(?<=a=\s)\d+[.]\d+',line)
    dt_re = re.search(r'(?<=dt=\s\s)[\d\.\de\-]+',line)
    if E_re:
        E_predkor_list.append(float(E_re.group()))
    if dt_re:
        dt_predkor_list.append(float(dt_re.group()))
#print(dt_kox_list)
plt.scatter(dt_predkor_list, E_predkor_list, color="red")
plt.hlines(0,0,max(max(dt_predkor_list), max(dt_kox_list)))
plt.show()