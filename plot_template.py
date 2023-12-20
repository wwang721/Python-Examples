#
#   Created by WW on 2023-12-19.
#   Copyright © WW. All rights reserved.
#
#   Template of python plotting
#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

plt.rcParams.update({
    # requires a working LaTeX installation & slower than Matplotlib's mathtext
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "DejaVu Sans"
})

plt.rcParams['figure.constrained_layout.use'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['xtick.top'] = True
plt.rc('xtick', labelsize=12, direction='in')
plt.rc('ytick', labelsize=12, direction='in')
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=12)

fig = plt.figure(figsize=(4, 3))
ax = plt.subplot(1, 1, 1)

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
yp = np.cos(x)

ax.plot(x, y, 'o', color='C0', markerfacecolor='none',
        linestyle='solid', linewidth=1.2, clip_on=False, label=r'$\sin (x)$')
ax.plot(x, yp, '^', color='C3', markerfacecolor='none',
        linestyle='dashed', linewidth=1.2, clip_on=False, label=r'$\cos (x)$')

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)
ax.set_xlabel(r"Coordinate $x\,\rm{[\mu m]}$")
ax.set_ylabel(r"Value $y\,\rm{[\mu m]}$")

ax.set_xticks([0, np.pi, 2*np.pi])

ax.set_xticklabels([r'$0$', r'$\pi$', r'$2\pi$'])
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.yaxis.set_minor_locator(AutoMinorLocator(2))

ax.set_yticks([-1, 0, 1])
ax.set_title(r'Trigonometric function', pad=15)
plt.legend(frameon=False)

plt.savefig("template.pdf", dpi=300)
