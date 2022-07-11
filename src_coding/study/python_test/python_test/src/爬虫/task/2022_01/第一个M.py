'''
@author king_xiong
@date 2022-01-16 22:37
'''
# 2 、第二种方案是给出具体的函数形式(可以是任意的，只要你能写的出来 下面的func就是)，用最小二乘的方式去逼近和拟合，求出函数的各项系数，如下：
#使用curve_fit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 导入log函数  np.log可以直接用
# from math import log
'''
np.abs(x)、np.fabs(x) ： 计算数组各元素的绝对值
np.sqrt(x) ： 计算数组各元素的平方根
np.square(x) ： 计算数组各元素的平方
np.log(x) 、np.log10(x)、np.log2(x) ： 计算数组各元素的自然对数、10底对数和2底对数
np.ceil(x) 、np.floor(x) ： 计算数组各元素的ceiling值或floor值
————————————————
原文链接：https://blog.csdn.net/brucewong0516/article/details/79186176
'''
import math

A=35
M=52.315
E=0.0105

#自定义函数 log(x) 等价于ln(x)
def func(x, a, b, A_0 ,E):
    return (a*420+b*np.log(420)-a*x-b*np.log(x))/(E*a*b)

#定义x、y散点坐标  x是浓度，y是时间
t = [0,15,30,60,90,120,150,180]
num = [420,256, 215, 202, 197, 186, 184, 177]

y = np.array(t)
x = np.array(num)

#非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
#获取popt里面是拟合系数
print(popt)
a = popt[0]
b = popt[1]

yvals = func(x, a, b, A_0=420,E=0.0634) #拟合y值
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)

print('系数pcov:', pcov)
print('系数yvals:', yvals)


# 绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=1) #指定legend的位置右下角
plt.title('curve_fit')

plt.show()