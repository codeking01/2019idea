# 变量不需要声明  直接可以用
# 但是需要赋值了以后才可以用
a=10
print(a)
b=type(a)
print(b)
print(type(12313))
print(type('true'))
c=id(b)
print(c)
# type()   value()  id()

a=11.6
a=int(a)
print('a=',a)
print('a的类型是',type(a))
##强制类型转化
# str() bool() int() float()
a='hello'
a=str(a)
print('a=',a)
print('a的类型',type(a))

b='123'
b=bool(b)
print('b=',b)
################
b=''
b=bool(b)
print('b=',b)
print('b的类型',type(b))
##
c=10/3 #保留小数位
print('c',c)
d=10//3  #整除
print('d=',d)
d=10**2 #取得幂次方
d=100**0.5 #开根号
#  %取模
