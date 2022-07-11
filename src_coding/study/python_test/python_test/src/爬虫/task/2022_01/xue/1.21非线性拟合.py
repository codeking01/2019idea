'''
@author king_xiong
@date 2022-01-21 20:38
'''
# 作者：星语者v
# 链接：https://www.zhihu.com/question/370155873/answer/1002737452
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# 自定义函数 e指数形式
def func(x, a, b):
    return (a * 411.2 + b * np.log(411.2) - a * x - b * np.log(x)) / (0.0634 * a * b)


# 定义x、y散点坐标
t = [ 3, 6, 9, 12, 15, 18, 21, 24, 30, 45, 60, 75, 105, 120]
x = np.array(t)
num = [ 242.5367233, 222.0592193, 186.7469012, 183.0464274, 176.1315181, 162.4779123, 137.322049,
       128.1086245, 116.9917119, 91.67899956, 98.44674202, 96.94215379, 75.70267361, 69.2011871]

y = np.array(num)
# 非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
# 获取popt里面是拟合系数
print(popt)
a = popt[0]
b = popt[1]

yvals = func(x, a, b)
# 拟合y值
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)

print('系数pcov:', pcov)
print('系数yvals:', yvals)
# 绘图
plot1 = plt.plot(x, y, 'r', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=1)
# 指定legend的位置右下角
plt.title('curve_fit')
plt.show()
