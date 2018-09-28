import ctypes
import time
myDLL = ctypes.cdll.LoadLibrary("./Dynamic Link Library/lib/myDLL.so")

rates = range(1,101)

for rate in rates:
	myDLL.procBar(rate)
	time.sleep(0.02)


print()