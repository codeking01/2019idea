'''
@author king_xiong
@date 2022-01-16 20:50
'''
import math

import numpy as np

import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

import pandas as pd


# 自定义函数 e指数形式

#自定义函数 log(x) 等价于ln(x)
def func(x, a, b ):
    return ((52.315+b*35)*np.log(35)+(a-b)*35-(52.315+b*35)*np.log(x)-(a-b)*x)/(0.0105*52.315*a)

#定义x、y散点坐标  x是浓度，y是时间
t = [30,60,90,120,150,180]
num = [19.14,17.01,16.01,15,12.52,10.79]

y = np.array(t)
x = np.array(num)

# 定义x、y散点坐标

# x = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
# x = np.array(x)
# x = np.array(range(20))
print('x is :\n', x)
# num = [536, 529, 522, 516, 511, 506, 502, 498, 494, 490, 487, 484, 481, 478, 475, 472, 470, 467, 465, 463]
# y = np.array(num)
print('y is :\n', y)

popt, pcov = curve_fit(func, x, y)

# 获取popt里面是拟合系数

a = popt[0]
b = popt[1]


yvals = func(x, a, b)   # 拟合y值

print(u'系数a:', a)
print(u'系数b:', b)

# 绘图
plot1 = plt.plot(x, y, 's', label='original values')

plot2 = plt.plot(x, yvals, 'r', label='polyfit values')

plt.xlabel('x')

plt.ylabel('y')

plt.legend(loc=1)  # 指定legend的位置右下角

plt.title('curve_fit')

plt.show()

