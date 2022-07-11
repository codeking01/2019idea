'''
@author king_xiong
@date 2022-01-16 22:29
'''
#自定义函数 log(x) 等价于ln(x)
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy import stats

def func(x, a, b, A_0 ,M,E):
    return ((M+b*A_0)*np.log(35)+(a-b)*35-(M+b*A_0)*np.log(x)-(a-b)*x)/(E*M*a)

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

# def myfunc(x):
#     return slope * x + intercept

mymodel = list(map(func, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
