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
import sklearn
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
def func(x, a, b ):
    return ((52.315+b*35)*np.log(35)+(a-b)*35-(52.315+b*35)*np.log(x)-(a-b)*x)/(0.0105*52.315*a)

#定义x、y散点坐标  x是浓度，y是时间
t = [0,30,60,90,120,150,180]
# num = [35,19.14,17.01,16.01,15,12.52,10.79]
num = [35,19.14129661,17.01110907,16.01429086,14.99497215,12.52311004,10.78682735]
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


# a =sklearn.ols(func,)