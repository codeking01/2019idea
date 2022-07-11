'''
@author king_xiong
@date 2022-01-17 15:05
'''
import numpy as np
import matplotlib.pyplot as plt
# # 定义x、y散点坐标
# x = [10,20,30,40,50,60,70,80]
# x = np.array(x)
# print('x is :\n',x)
# num = [174,236,305,334,349,351,342,323]
# y = np.array(num)
# print('y is :\n',y)
# #用3次多项式拟合
# f1 = np.polyfit(x, y, 3)
# # print('f1 is :\n',f1)
# p1 = np.poly1d(f1)
# # print('p1 is :\n',p1)
#
# #也可使用yvals=np.polyval(f1, x)
# yvals = p1(x) #拟合y值
# print('yvals is :\n',yvals)
# #绘图
# plot1 = plt.plot(x, y, 's',label='original values')
# plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc=4) #指定legend的位置右下角
# plt.title('polyfitting')
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#自定义函数 e指数形式

def func(x, a, b,c):
    return a*np.sqrt(x)*(b*np.square(x)+c)
#定义x、y散点坐标

x = [20,30,40,50,60,70]

x = np.array(x)

num = [453,482,503,508,498,479]

y = np.array(num)
#非线性最小二乘法拟合

popt, pcov = curve_fit(func, x, y)

#获取popt里面是拟合系数

print(popt)
a = popt[0]

b = popt[1]

c = popt[2]

yvals = func(x,a,b,c) #拟合y值

print('popt:', popt)

print('系数a:', a)
print('系数b:', b)

print('系数c:', c)

print('系数pcov:', pcov)

print('系数yvals:', yvals)
#绘图

plot1 = plt.plot(x, y, 's',label='original values')

plot2 = plt.plot(x, yvals, 'r',label='polyfit values')

plt.xlabel('x')
plt.ylabel('y')

plt.legend(loc=4) #指定legend的位置右下角

plt.title('curve_fit')

plt.show()

