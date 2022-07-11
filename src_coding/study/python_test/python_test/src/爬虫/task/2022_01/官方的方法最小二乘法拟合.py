'''
@author king_xiong
@date 2022-01-17 16:36
'''
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


# 定义需要拟合的函数
def func(x, a, b ):
    return (a*420+b*np.log(420)-a*x-b*np.log(x))/(0.0634*a*b)


# Define the data to be fit with some noise:
# 用numpy的random库生成干扰
xdata =[420, 255.5261415, 215.2780169, 201.9100312, 197.4446766, 186.1786607, 183.8264103, 176.7531996]
y = func(xdata)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')
# Fit for the parameters a, b, c of the function func:

popt, pcov = curve_fit(func, xdata, ydata)
print(popt)

plt.plot(xdata, func(xdata, *popt), 'r-',
         label='fit: a=%5.3f, b=%5.3f ' % tuple(popt))
# Constrain the optimization to the region of 0 <= a <= 3, 0 <= b <= 1 and 0 <= c <= 0.5:
# 限定范围进行拟合
# popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
popt, pcov = curve_fit(func, xdata, ydata)
print(popt)

plt.plot(xdata, func(xdata, *popt), 'g--',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()