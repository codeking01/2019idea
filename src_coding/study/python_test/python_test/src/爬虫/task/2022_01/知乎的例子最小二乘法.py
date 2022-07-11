'''
@author king_xiong
@date 2022-01-17 16:48
'''
# 引用库函数
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as op

# 需要拟合的数据组
x_group = np.array([420, 255.5261415, 215.2780169, 201.9100312, 197.4446766, 186.1786607, 183.8264103, 176.7531996])
y_group = np.array([0, 15, 30, 60, 90, 120, 150, 180])


# 需要拟合的函数
def func(x, a, b):
    return (a * 420 + b * np.log(420) - a * x - b * np.log(x)) / (0.0634 * a * b)


# 得到返回的A，B值
A, B = op.curve_fit(func, x_group, y_group)
# 求系数
a = A[0]
b = A[1]
print(a,b)

# 数据点与原先的进行画图比较
plt.scatter(x_group, y_group, marker='o', label='real')
x = np.array([420, 255.5261415, 215.2780169, 201.9100312, 197.4446766, 186.1786607, 183.8264103, 176.7531996])
y = (a * 420 + b * np.log(420) - a * x - b * np.log(x)) / (0.0634 * a * b)
plt.plot(x, y, color='red', label='curve_fit')
plt.legend()
plt.title('%.5fx%.5f=y' % (a, b))
plt.show()
