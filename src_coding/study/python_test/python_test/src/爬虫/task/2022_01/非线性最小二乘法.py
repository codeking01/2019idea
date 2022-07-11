'''
@author king_xiong
@date 2022-01-15 11:02
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b):
    return (a*420+b*np.log(420)-a*x-b*np.log(x))/(0.0634*a*b)
#定义x、y散点坐标
x = [420 ,255.5261415, 215.2780169, 201.9100312, 197.4446766 ,186.1786607, 183.8264103 ,176.7531996]
x = np.array(x)

num = [0,15,30,60,90,120,150,180]
y = np.array(num)

# 加入噪音数据
# rng = np.random.default_rng()
# y_noise = 0.2 * rng.normal(size=x.size)
# ydata = y + y_noise
plt.plot(x, y, 'b-', label='data')
popt, pcov = curve_fit(func, x, y)
print(popt)
plt.show()

##非线性最小二乘法拟合
# popt, pcov = curve_fit(func, x, y)
# #获取popt里面是拟合系数
# print(popt)
# a = popt[0]
# b = popt[1]
# yvals = func(x,a,b) #拟合y值
# print('popt:', popt)
# print('系数a:', a)
# print('系数b:', b)
#
# print('系数pcov:', pcov)
# print('系数yvals:', yvals)
# plot1 = plt.plot(x, y, 's',label='original values')
# plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc=1) #指定legend的位置右下角
# plt.title('curve_fit')
# plt.show()
