import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

N = 1000
thickness = 200
data = np.zeros((N+1, N+1))
for i in range(N+1):
	for j in range(N+1):
		xx = i - N/2
		yy = j - N/2
		r = np.linalg.norm((xx, yy))
		data[i, j] = 0.5 * np.tanh((N/4 - r)/thickness) + 0.5

x = np.linspace(-N/2, N/2, N+1)
y = np.linspace(-N/2, N/2, N+1)

X, Y = np.meshgrid(x, y)

rgb=([255,255,255],
	[255,251,240],
	[243,249,241],
	[252,239,248],
	[214,236,240],
	[224,240,233],
	[194,204,208],
	[176,185,185],
	[117,138,153],
	[128,128,128])
rgb=np.array(rgb)/255.0
icmap=colors.ListedColormap(rgb, name='my_color') 

plt.figure()
plt.imshow(data, cmap=icmap, origin="lower", extent=(-N/2, N/2, -N/2, N/2), vmax=1., vmin=0)
plt.colorbar()
plt.savefig("colorbar.pdf", dpi=300)
