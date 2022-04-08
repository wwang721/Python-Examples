import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', **{'family': 'sans-serif',
                  'sans-serif': ['DejaVu Sans']})  # sans-serif

plt.rcParams['figure.constrained_layout.use'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['xtick.top'] = True
plt.rc('xtick', labelsize=12, direction='in')
plt.rc('ytick', labelsize=12, direction='in')
plt.rc('axes', labelsize=14)

v0 = np.array([0.556, 1.556, 2.556, 3.556, 4.556, 5.556]) * 1e-2
Dr = 5.555e-3
R = 7

Pe = (v0 / Dr)/R

A = [0, 0, 1, 1.80952, 3.16, 3.8022]
rupture_rate = [0, 0, 3./100, 21./100, 75./98, 91./99]


fig = plt.figure()
ax1 = fig.add_subplot(111)
lax = ax1.plot(Pe, A, "-o", label="Averaged cluster size", clip_on=False)
ax1.set_ylim(0, 4)
ax1.set_xlabel("Pe")
ax1.set_ylabel("A")


ax2 = ax1.twinx()
ax2.plot(Pe, rupture_rate, "-s")
rax = ax2.plot(Pe, rupture_rate, "-s", label="Rupture rate", clip_on=False)
ax2.set_ylim(0, 1.)
ax2.set_ylabel("K", rotation=270, labelpad=15)

ax = lax + rax
labs = [a.get_label() for a in ax]
ax1.legend(ax, labs, loc=0, frameon=False)

plt.savefig("test.png", dpi=300)
