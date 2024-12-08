#
#   Created by WW on 2023-12-19.
#   Updated by WW on 2024-12-08.
#   Copyright © WW. All rights reserved.
#
#   Template of python plotting
#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from plt_setting import plt_init

plt_init()

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

# use two different math font families
ax.text(3.5, 0.7, r"$\left< n^2\right>-\left< n\right>^2$", fontsize=12)
ax.text(3.5, 0.5, r"$\left< n^2\right>-\left< n\right>^2$", fontsize=12, math_fontfamily='stix')

ax.set_yticks([-1, 0, 1])
ax.set_title(r'Trigonometric function', pad=15)
plt.legend(frameon=False)

plt.savefig("v1_trig_func.svg", dpi=300)
