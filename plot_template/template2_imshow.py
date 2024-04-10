import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from plt_setting import plt_init

plt_init()

plt.figure(figsize=(4, 3))
ax = plt.subplot(1, 1, 1)

FN = np.load("FN_mle.npy")

chis = np.linspace(0.01, 0.98, 20)
alphas = np.linspace(0.03, 1, 20)

dy = (0.98-0.01)/19
dx = (1.-0.03)/19

background = ax.imshow(FN, origin='lower', extent=(
    0.03-(dx/2), 1+(dx/2), 0.01-(dy/2), 0.98+(dy/2)), vmin=0, vmax=1, cmap=cm.coolwarm, zorder=1)

ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels(['$0$', '$0.5$', '$1$'])
ax.set_yticks([0, 0.5, 1])
ax.set_yticklabels(['$0$', '$0.5$', '$1$'])

ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.yaxis.set_minor_locator(AutoMinorLocator(2))

X, Y = np.meshgrid(alphas, chis)
ax.contour(X, Y, FN, [0.1], linewidths=1.5,
           colors="k", zorder=2, linestyles='dashed')

cbar = plt.colorbar(background, ax=ax, ticks=np.linspace(0, 1., 3))
cbar.ax.yaxis.set_minor_locator(AutoMinorLocator(2))
cbar.ax.tick_params(axis='y', which='both', direction='out')
cbar.ax.tick_params(axis='y', which='major', width=0.3, length=3)
cbar.ax.tick_params(axis='y', which='minor', width=0.1, length=1.5)
cbar.ax.set_yticklabels(['$0$', '$0.5$', '$1$'])
cbar.outline.set_linewidth(0)

cbar.set_label(
    r"False negative rate $\mathrm{FNR}$", rotation=270, labelpad=15)

ax.set_xlabel(r"Unbinding rate ratio $\alpha=r/r'$")
ax.set_ylabel(r"Correct ligand fraction $\chi=c_0/c_t$")
ax.set_title(r"$\sigma = 1\,\mathrm{\mu m}$", fontsize=16, pad=10)

# set aspect ratio to 1
ratio = 1.
y_low, y_high = ax.get_ylim()
x_left, x_right = ax.get_xlim()
ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)
# ax.set_aspect('auto')

plt.savefig("FNR_imshow.pdf", dpi=300)
