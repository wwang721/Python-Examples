import numpy as np
import time 
from sympy import *
a,b,c=map(float,input('输入积分上下限及步长:').split())
s=0
x=Symbol('x',real=True)
c1=Symbol('c1',real=True)
c2=Symbol('c2',real=True)
t=Symbol('t',real=True)
d=Symbol('d',real=True)
start=time.clock()
for v in np.arange(a,b,c):
	nm=c1*(E**(-x/(v*t)))+c2*(E**(-(d-x)/(v*t)))
	s=s+nm*c
print('ans=',s)
end=time.clock()
print('计算所用时间:{}s'.format(end-start))
