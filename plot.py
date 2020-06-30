import numpy as np 
import matplotlib.pyplot as plt 

print(plt.style.available)

plt.style.use("ggplot")

# For SCI Plots
# pip install SciencePlots
# https://github.com/garrettj403/SciencePlots
plt.style.use('science')
# or you can use two styles: plt.style.use(['science', 'ieee'])


x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4), dpi=200)

plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label=r"$cos(x^2)$")	#matplot自带LaTex编译器但是调用会大大减慢绘图速度,有时latex不能识别则在""前加r

plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("Pyplot First Example")
plt.ylim(-1.2,1.2)

#令图例显示在图像外侧
plt.legend(loc=2, bbox_to_anchor=(1.02, 1), borderaxespad=0)
#loc=2代表图例的取点定位为图例框的左上角，bbox_to_anchor代表取点的横纵坐标(按比例)，borderaxespad代表边缘的空白

#plt.show()   #show之后必须关闭绘图窗口才能继续程序，不过这样就无法savefig了

plt.savefig("test.png", dpi=200, bbox_inches="tight")	#bbox_inches="tight"保证图例不会被切掉一半
