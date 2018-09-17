import numpy as np
from scipy import optimize		#最小二乘法拟合
import matplotlib.pyplot as plt 	#python绘图 	
from matplotlib.font_manager import FontProperties 		#绘图字体管理

font = FontProperties(fname=r"/Library/Fonts/Songti.ttc",size=14) 	#导入系统中的宋体字体

def func(x, p):
	'''
	数据拟合所用的函数：A*exp(-x/lambda)
	'''
	A, lam = p
	return A*np.exp(-x/lam)

def residuals(p, y, x):
	'''
	实验得到y和拟合函数之间的差，p为拟合需要找到的所有系数
	'''
	return y-func(x,p)

#------------------------------------------------------------------------------
"""导入实验原始数据"""
f1 = open(r'/Users/wangwei/Desktop/cuda/data/x.txt','r')
lines = f1.readlines()
x = [float(line.strip()) for line in lines]
f1.close()

mode = input("Injection mode:")
R = input("R:")
Beta = input("Beta:")

f2 = open(r'/Users/wangwei/Desktop/cuda/data/Fx/Fx_injectionmode{}/Fx_R{}/Fx_Beta{}/0-Fx-mode({})R({})Beta({})dBeta(0).txt'.format(mode,R,Beta,mode,R,Beta),'r')
lines = f2.readlines()
y = [float(line.strip()) for line in lines]
f2.close()

x=np.array(x)

y=np.array(y)     #将导入数据从list转化为array

#------------------------------------------------------------------------------
#最小二乘法拟合

plsq = optimize.leastsq(residuals, [50,10], args=(y,x))

A, lam = plsq[0]

print("拟合结果:\nA={}".format(A))

print("lambda={}".format(lam))

#------------------------------------------------------------------------------

#绘图
xp = np.linspace(0.01,80,100)
yp = func(xp, [A, lam])

plt.figure(figsize=(8,6), dpi=100)

plt.plot(x, y, label="原始数据", linewidth=2)
plt.plot(xp, yp, label="拟合图像", linewidth=2)

plt.xlabel("x/μm")
plt.ylabel("fx")

plt.legend(prop=font) 	#将label中的汉字字体设置为导言区导入的宋体字体

plt.show()

