import matplotlib.pyplot as plt 	#导入matplot绘图库

#-----------------------------------------------------------------------------
'''导入x数据'''

f1 = open(r'/Users/wangwei/Desktop/cuda/data/x.txt','r')
lines = f1.readlines()
x = [float(line.strip()) for line in lines]	#string经过strip或split处理后强制转化为float组成list
f1.close()
#-----------------------------------------------------------------------------

print('1.Gx  2.Fx  3.Jm  4.exit')
choice = int(input("Input:"))

if choice == 4:
	exit()

mode = input("Injection Mode:")
R = input("R:")

if choice == 1:
	rs = R.strip().split()

	plt.figure(figsize=(8,6), dpi=100)

	for r in rs:
		f2 = open(r'/Users/wangwei/Desktop/cuda/data/Gx/Gx_mode({})/gx-mode({})R({}).txt'.format(mode,mode,r),'r')
		lines = f2.readlines()
		y = [float(line.strip()) for line in lines]
		f2.close()
		
		plt.plot(x, y, label="R={}".format(r), linewidth=2)
	
	plt.xlabel("x/μm")
	plt.ylabel("gx")
	plt.legend()

	plt.savefig(r'/Users/wangwei/Documents/Python/plot/figures/gx-mode({})R({}).png'.format(mode,R), dpi=100)

elif choice == 2:
	Beta = input("Beta:")
	betas = Beta.strip().split()

	plt.figure(figsize=(8,6), dpi=150)

	for beta in betas:
		f2 = open(r'/Users/wangwei/Desktop/cuda/data/Fx/Fx_injectionmode{}/Fx_R{}/Fx_Beta{}/0-Fx-mode({})R({})Beta({})dBeta(0).txt'.format(mode,R,beta,mode,R,beta),'r')
		lines = f2.readlines()
		y = [float(line.strip()) for line in lines]
		f2.close()
	
		plt.plot(x, y, label="Beta={}".format(beta), linewidth=1.5)

	plt.xlabel("x/μm")
	plt.ylabel("fx")
	plt.legend()

	plt.savefig(r'/Users/wangwei/Documents/Python/plot/figures/fx-mode({})R({})Beta({}).png'.format(mode,R,Beta), dpi=150)

elif choice == 3:
	Beta = input("Beta:")
	betas = Beta.strip().split()

	plt.figure(figsize=(8,6), dpi=150)

	for beta in betas:
		f2 = open(r'/Users/wangwei/Desktop/cuda/data/jm/jm_injectionmode{}/jm_R{}/jm_Beta{}/0-jm-mode({})R({})Beta({})dBeta(0).txt'.format(mode,R,beta,mode,R,beta),'r')
		lines = f2.readlines()
		y = [float(line.strip()) for line in lines]
		f2.close()
	
		plt.plot(x, y, label="beta={}".format(beta), linewidth=1.5)
	
	plt.xlabel("x/μm")
	plt.ylabel("jm")
	plt.legend()
	
	plt.savefig(r'/Users/wangwei/Documents/Python/plot/figures/jm-mode({})R({})Beta({}).png'.format(mode,R,Beta), dpi=150)

print('Done.\n')

#-----------------------------------------------------------------------------
#Mac下python的清屏命令
'''
import os
os.system("clear")
'''
#-----------------------------------------------------------------------------
	
















