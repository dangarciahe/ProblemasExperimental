import matplotlib.pyplot as plt
import matplotlib.font_manager
import numpy as np
import matplotlib


def I_I0(gamma, dz):
    return 1+gamma*np.cos(2*np.pi*dz)

Dz = np.linspace(0, 5, 100)
a = np.array([0.001,0.01, 0.1, 1])
gamma = 2*np.sqrt(a)/(a+1)

fig = plt.figure()
gs = fig.add_gridspec(4, hspace=0.1)
axs = gs.subplots(sharex=True, sharey=True)
axs[0].plot(Dz, I_I0(gamma[0], Dz))
axs[0].set_title(r'$\mathrm{I_{1}/I_{2}=10^{-3}}$', loc='center', x=0.53, y=0.63)
axs[1].plot(Dz, I_I0(gamma[1], Dz))
axs[1].set_title(r'$I_{1}/I_{2}=10^{-2}$', loc='center', x=0.53, y=0.56)
axs[2].plot(Dz, I_I0(gamma[2], Dz))
axs[2].set_title(r'$I_{1}/I_{2}=10^{-1}$', loc='center', x=0.53, y=0.65)
axs[2].text(-0.8, 2, r'$I/I_{0}$', fontsize=13 ,rotation='vertical')
axs[3].plot(Dz, I_I0(gamma[3], Dz))
axs[3].set_title(r'$I_{1}/I_{2}=1$', loc='center', x=0.5, y=0.67)
axs[3].text(2.1,-1.2, r'${\Delta z}{(\lambda/2)^{-1}}$', fontsize=13)
# Hide x labels and tick labels for all but bottom plot.
for ax in axs:
    ax.label_outer()
#plt.show()
plt.savefig('I_I0.pdf')
