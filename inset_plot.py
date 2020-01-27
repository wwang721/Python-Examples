#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Created by WW on Jan. 22, 2020
# All rights reserved.
#

import numpy as np
import matplotlib.pyplot as plt 
#from mpl_toolkits.axes_grid1.inset_locator import inset_axes	# for inset plot
from matplotlib.ticker import MultipleLocator, FormatStrFormatter # for ticks format

#-----------------------------------------------------------------------------
'''import data'''
'''
f1 = open(r'lambda.txt','r')
lines = f1.readlines()
x = [float(line.strip().split()[0]) for line in lines]	#string经过strip或split处理后强制转化为float组成list
y = [float(line.strip().split()[1]) for line in lines]
f1.close()
'''

data = np.loadtxt(r"lambda.csv", delimiter=',')
x = data[:,0]
y = data[:,1] 

#-----------------------------------------------------------------------------

fig = plt.figure(figsize=(8, 6))

# 设置xtick和ytick的方向：in、out、inout
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'out'

Formatter = FormatStrFormatter('%g') # tick label format

#-----------------------------------------------------------------------------
'''main figure'''

ax1 = fig.add_subplot(1, 1, 1)

ax1.plot(x, y,  "-o", color="tomato", linewidth=1.5)

ax1.set_xlabel(r"$T/K$")
ax1.set_ylabel(r"$\lambda/\mu m$")
ax1.set_title(r"$\lambda$-$T$ Figure")

ax1.set_xlim(0,300)
ax1.set_ylim(5.8,8.4)
ax1.set_xticks(np.arange(25,300,50), minor="True")	# show minor ticks
ax1.set_yticks(np.arange(6.25,8.26,0.5), minor="True") # show minor ticks

ax1.grid(True) # show major tick grid 
ax1.grid(True, which="minor", linestyle="--") # show minor tick grid

#-----------------------------------------------------------------------------
'''inset figure'''

#ax2 = inset_axes(ax1, width=3, height=2.3, loc="upper right") # use inset_axes() directly

ax2 = fig.add_axes([0.5,0.5,0.385,0.36]) # position: left, bottom, width, height (range 0 to 1)

ax2.plot(x, y, "-o", color="deepskyblue", linewidth=1.5)
ax2.set_xlim(10,60)
ax2.set_ylim(7.35,8.25)

ax2.xaxis.set_major_formatter(Formatter) # major ticks label format
ax2.set_xticks(np.arange(15,60,10), minor="True") # show minor ticks
ax2.set_yticks(np.arange(7.5,8.2,0.2), minor="True") # show minor ticks

ax2.grid(True, linestyle="-.") # show major tick grid
#ax2.grid(True, which="minor", linestyle="--")

plt.savefig(r'lambda.eps')
















