import matplotlib.pyplot as plt
import numpy as np


a = 25
w = 1000

q0=0.002
t = np.linspace(0,0.1,1000)
q = q0*np.exp(-a*t)*np.cos(w*t)
qp = q0*np.exp(-a*t)
I = q0*np.exp(-a*t)*(a*np.cos(w*t)+w*np.sin(w*t))


fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_xlabel(r"$t/\rm s$")
ax1.set_ylabel(r"$q(t)/\rm C$")

lns1 = ax1.plot(t,q, label=r"$q(t)$", zorder=1)

ax1.plot(t,qp, "--", color="gray", zorder=0, alpha=0.8)
ax1.plot([0,1],[0,0],"--", color="gray", zorder=0, alpha=0.8)
ax1.plot(t,-qp, "--", color="gray", zorder=0, alpha=0.8)

ax1.set_xlim(0, 0.1)
ax1.set_ylim(-0.002,0.002)

ax2 = ax1.twinx()

lns2 = ax2.plot(t,I, color="orange", label=r"$I(t)$", zorder=2)

ax2.set_ylabel(r"$I(t)/\rm A$")
ax2.set_ylim(-2,2)

# combines legends
lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)

plt.savefig("twinx.pdf",dpi=300, bbox_inches="tight")
