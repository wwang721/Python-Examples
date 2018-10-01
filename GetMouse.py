import os
import tkinter as tk
import pyautogui as pag
 
def nextRoot4():
	def nextRoot3():
		global fp, A
		A = os.path.dirname(os.path.realpath(sys.argv[0]))
		fp = open(r'{}/points.txt'.format(A),'w')

		root4.destroy()
		root3 = tk.Tk()
		root3.title("GetMouse")
		root3.geometry("230x290")

		#-----------------------------------------------------------------------
		frm6 = tk.Frame(root3)

		tk.Label(frm6, text="", font=("Songti", 5)).pack(side=tk.LEFT)

		frm6.pack(side=tk.TOP)

		#-----------------------------------------------------------------------
		frm7 = tk.Frame(root3)

		tk.Label(frm7, text="按下回车键确定坐标", font=("Songti", 12)).pack(side=tk.TOP)

		frm7.pack(side=tk.TOP)

		#-----------------------------------------------------------------------
		frm8 = tk.Frame(root3)

		global num,xs,ys
		num = 1
		xs = []
		ys = []
		def print_item(event):	
			global num, x0p, y0p, xmax, ymax, xmaxp, ymaxp, xs, ys
			xp,yp = pag.position()
			x = (xp - x0p) * xmax / (xmaxp - x0p)
			y = (yp - y0p) * ymax / (ymaxp - y0p)
			lb.insert(tk.END,"{:>2}.({:>6.2f},{:>6.2f})".format(num,x,y))
			fp.writelines("{:.2f}\t{:.2f}\n".format(x,y))
			xs.append(x)
			ys.append(y)
			num = num + 1

		var3 = tk.StringVar()
		lb = tk.Listbox(frm8, height=13, selectmode = tk.SINGLE, listvariable = var3)

		root3.bind('<Return>',print_item)
		#------------------------------------------------------------------
		#tk.Scrollbar
		scrl = tk.Scrollbar(frm8)
		scrl.pack(side=tk.RIGHT, fill= tk.Y)	#Y表示竖直方向


		lb.configure(yscrollcommand = scrl.set)
		lb.pack(side=tk.LEFT, fill=tk.BOTH)
		scrl['command'] = lb.yview

		frm8.pack(side=tk.TOP)
		#------------------------------------------------------------------

		tk.Button(root3, text="完成",font=("Songti", 12),  command=root3.destroy, width=5).pack(side=tk.TOP)

		root3.mainloop()

		#-----------------------------------------------------------------------
		root2 = tk.Tk()
		root2.title("GetMouse")
		root2.geometry("250x85")

		#-----------------------------------------------------------------------
		frm3 = tk.Frame(root2)

		tk.Label(frm3, text="", font=("Songti", 5)).pack(side=tk.LEFT)

		frm3.pack(side=tk.TOP)

		#-----------------------------------------------------------------------
		frm4 = tk.Frame(root2)

		tk.Label(frm4, text="是否保存数据？", font=("Songti", 12)).pack(side=tk.TOP)

		frm4.pack(side=tk.TOP)

		#-----------------------------------------------------------------------
		frm5 = tk.Frame(root2)

		def saveYes():
			global fp
			root2.destroy()
			fp.close()
		def saveNo():
			global fp,A
			root2.destroy()
			fp.close()
			os.remove(r'{}/points.txt'.format(A))

		tk.Button(frm5, text="是",font=("Songti", 12),  command=saveYes, width=5).pack(side=tk.LEFT)
		tk.Button(frm5, text="否",font=("Songti", 12),  command=saveNo, width=5).pack(side=tk.RIGHT)

		frm5.pack(side=tk.TOP)

		root2.mainloop()
	#-----------------------------------------------------------------------
	global xmax, ymax
	xmax = float(var1.get())
	ymax = float(var2.get())

	root.destroy()
	root4 = tk.Tk()
	root4.title("GetMouse")
	root4.geometry("270x120")

	#-----------------------------------------------------------------------
	frm9 = tk.Frame(root4)

	tk.Label(frm9, text="", font=("Songti", 5)).pack(side=tk.LEFT)

	frm9.pack(side=tk.TOP)

	#-----------------------------------------------------------------------
	frm10 = tk.Frame(root4)

	tk.Label(frm10, text="按下回车键分别确定原点、Xmax、Ymax坐标", font=("Songti", 12)).pack(side=tk.TOP)

	frm10.pack(side=tk.TOP)

	#-----------------------------------------------------------------------
	frm11 = tk.Frame(root4)

	global num2
	num2 = 1
	def getPoint(event):
		global num2, x0p, y0p, xmaxp, ymaxp
		xp,yp = pag.position()
		lb2.insert(tk.END,"({:>5},{:>5})".format(xp,yp))
		if num2 == 1:
			x0p = xp
			y0p = yp
		elif num2 == 2:
			xmaxp = xp
		elif num2 == 3:
			ymaxp = yp
		num2 = num2 + 1


	var4 = tk.StringVar()
	lb2 = tk.Listbox(frm11, height=3, selectmode = tk.SINGLE, listvariable = var4)
	
	root4.bind('<Return>',getPoint)
	lb2.pack(side=tk.TOP)

	tk.Button(frm11, text="完成",font=("Songti", 12),  command=nextRoot3, width=5).pack(side=tk.TOP)

	frm11.pack(side=tk.TOP)

	root4.mainloop()




root = tk.Tk()
root.title("GetMouse")	
root.geometry("250x100")

#-----------------------------------------------------------------------
frm = tk.Frame(root)

tk.Label(frm, text="", font=("Songti", 5)).pack(side=tk.LEFT)

frm.pack(side=tk.TOP)

#-----------------------------------------------------------------------
frm1 = tk.Frame(root)
tk.Label(frm1, text="Xmax：", font=("Songti", 12)).pack(side=tk.LEFT)

var1 = tk.StringVar()
tk.Entry(frm1, textvariable = var1, width=10).pack(side=tk.LEFT)

frm1.pack(side=tk.TOP)

#-----------------------------------------------------------------------
frm2 = tk.Frame(root)
tk.Label(frm2, text="Ymax：", font=("Songti", 12)).pack(side=tk.LEFT)

var2 = tk.StringVar()
tk.Entry(frm2, textvariable = var2, width=10).pack(side=tk.LEFT)

frm2.pack(side=tk.TOP)


tk.Button(root, text="确定",font=("Songti", 12), command=nextRoot4, width=10).pack(side=tk.TOP)		
root.mainloop()


#-----------------------------------------------------------------------

















