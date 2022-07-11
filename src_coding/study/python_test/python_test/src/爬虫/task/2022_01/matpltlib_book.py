'''
@author king_xiong
@date 2022-01-17 13:48
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

t = [0,15,30,60,90,120,150,180]
num = [420,256, 215, 202, 197, 186, 184, 177]
y=t
x =num

plt.scatter(x, y)
# 调整坐标轴
# plt.axis([0,450,0,200])
# 后面的3代表自由度
mymodel = np.poly1d(np.polyfit(x, y,3))

myline = np.linspace(150,440, 200)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
mymodel = np.poly1d(np.polyfit(x, y,3))

print(r2_score(y, mymodel(x)))