'''
@author king_xiong
@date 2022-01-17 16:26
'''
'''
@author king_xiong
@date 2022-01-16 19:55
'''
# 作者：星语者v
# 链接：https://www.zhihu.com/question/370155873/answer/1002737452
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 2 、第二种方案是给出具体的函数形式(可以是任意的，只要你能写的出来 下面的func就是)，用最小二乘的方式去逼近和拟合，求出函数的各项系数，如下：
#使用curve_fit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sklearn

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
def func(x, a, b ):
    return (a*420+b*np.log(420)-a*x-b*np.log(x))/(0.0634*a*b)

#定义x、y散点坐标  x是浓度，y是时间-
# t = [0 ,15, 30, 60 ,90, 120, 150, 180]
t = [0, 3, 6, 9, 12, 15, 18, 21, 24, 30, 45, 60, 75, 105, 120]

# num = [35,19.14,17.01,16.01,15,12.52,10.79]
# num = [420, 255.5261415, 215.2780169, 201.9100312, 197.4446766, 186.1786607, 183.8264103, 176.7531996]
num = [411.1571085, 242.5367233, 222.0592193, 186.7469012, 183.0464274, 176.1315181, 162.4779123, 137.322049,
       128.1086245, 116.9917119, 91.67899956, 98.44674202, 96.94215379, 75.70267361, 69.2011871]

x = np.array(num)
y =np.array(t)


#非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
#获取popt里面是拟合系数
print(popt)
a = popt[0]
b = popt[1]
yvals = func(x,a,b)
#拟合y值print('popt:', popt)
print('系数a:', a)
print('系数b:', b)
print('系数pcov:', pcov)
print('系数yvals:', yvals)
#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=1)
#指定legend的位置右下角
plt.title('curve_fit')
plt.show()


# # R方要自己定义###定义R^2计算函数
# def r_squared(ydata,calc_ydata):
#     ###计算拟合度
#     ydata = [float(x) for x in ydata]
#     calc_ydata = [float(x) for x in calc_ydata]
#     residual = np.array(ydata)-np.array(calc_ydata)
#     #总平方和sst=ssr+sse
#     sst=np.sum((ydata-np.mean(ydata))**2)
#     #回归平方和
#     ssr=np.sum((calc_ydata-np.mean(ydata))**2)
#     #残差平方和
#     sse=np.sum(residual**2)
#     #print(ssr,sse,sst)
#     r_squared = ssr/sst
#     return r_squared
# print("++++",r_squared(ydata=y,calc_ydata=x))