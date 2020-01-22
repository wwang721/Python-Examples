import numpy as np 
import matplotlib.pyplot as plt 
from scipy import interpolate

xx = range(15)
lams = range(1,6) 

plt.figure(figsize = (7,5), dpi = 200)

for lam in lams:
    yy = []
    for x in xx:
        yy.append(np.exp(-lam) * (lam ** x) / np.math.factorial(x))
    
    func = interpolate.interp1d(xx, yy, kind = 'cubic') #插值
    xnew = np.arange(0.0, 10.2 ,0.1)
    ynew = func(xnew)

    plt.plot(xnew, ynew, label="$\lambda$={}".format(lam), linewidth=2)

plt.xlabel("$X$")
plt.ylabel("$P(X=k)$")
plt.title("Poisson Distribution")
plt.text(3.5, 0.3, r'$P(X=k)=\dfrac{\lambda^k}{k!}e^{-\lambda}, k=0,1,2...$')	#matplot自带LaTex编译器但是调用会大大减慢绘图速度,有时latex不能识别则在""前加r
plt.xlim(0,10)
plt.ylim(0.0, 0.45)

plt.legend() 

plt.savefig("Poisson.png", dpi=200)	
