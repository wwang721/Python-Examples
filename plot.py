import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4), dpi=200)

plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")	#matplot自带LaTex编译器但是调用会大大减慢绘图速度

plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("Pyplot First Example")
plt.ylim(-1.2,1.2)
plt.legend()

#plt.show()   #show之后必须关闭绘图窗口才能继续程序，不过这样就无法savefig了

plt.savefig("test.png", dpi=200)
