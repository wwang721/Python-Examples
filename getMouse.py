import os,sys
import pyautogui as pag
import ctypes

A = os.path.dirname(os.path.realpath(sys.argv[0])) #若使用pyinstaller生成执行文件后使用
#A="."

myDLL = ctypes.cdll.LoadLibrary("/Users/wangwei/Documents/Python/Dynamic Link Library/lib/myDLL.so")

os.system("clear")

fp = open(r'{}/points.txt'.format(A),'w')

#生成执行文件后经常出现嵌套exception所以用了嵌套try来避免这个问题
try:
	try:
		print("输入任意键确定原点O坐标：")
		myDLL.mygetch()
		x0p,y0p = pag.position()
		posStr = "Position:(" + str(x0p).rjust(4)+','+str(y0p).rjust(4)+")"
		print(posStr)
		print("按任意键继续...")
		myDLL.mygetch()
		os.system("clear")

		xmax = input("请输入xmax:")
		xmax = float(xmax)
		print("输入任意键确定xmax坐标：")
		myDLL.mygetch()
		xmaxp,y = pag.position()
		os.system("clear")

		ymax = input("请输入ymax:")
		ymax = float(ymax)
		print("请移动鼠标输入任意键确定ymax坐标：")
		myDLL.mygetch()
		x,ymaxp = pag.position()
		os.system("clear")

		print("开始获取数据...")
		print("Num     x      y")
		num = 1
		while 1:
			myDLL.mygetch()	
			xp,yp = pag.position() 	#返回鼠标的坐标
			x = (xp - x0p) * xmax / (xmaxp - x0p)
			y = (yp - y0p) * ymax / (ymaxp - y0p)
			print("{:>2}.({:>6.2f},{:>6.2f})".format(num,x,y))	#打印坐标
			fp.writelines("{:.2f}\t{:.2f}\n".format(x,y))
			num = num + 1
			
	except KeyboardInterrupt:	#输入Ctrl+C终止程序时执行
		ch = input("save data?(y/n)")
		if ch == 'y' or ch == 'yes':
			fp.close()
		else:
			os.remove(r'{}/points.txt'.format(A))
		print("end...")
except:
	ch = input("save data?(y/n)")
	if ch == 'y' or ch == 'yes':
		fp.close()
	else:
		os.remove(r'{}/points.txt'.format(A))
	print("end...")
