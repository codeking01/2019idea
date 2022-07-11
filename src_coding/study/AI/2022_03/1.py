'''
@author king_xiong
@date 2022-03-04 20:15
'''
from sympy import diff, symbols
t = symbols('t')
x = t**2/2
y = 1-t
f = diff(y,t)/diff(x,t)
print(f)
