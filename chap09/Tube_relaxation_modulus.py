# Relaxation modulus of Tube model

import numpy as np
import matplotlib.pyplot as plt

tau_R = 1.0  # Rouse緩和時間（これでスケールしたことにする）

# short-time limit of the Rouse relaxation modulus
def G_Tube_s(t, tau_R):
    G_s =  1 + (t/tau_R)**(-1/2)
    return G_s  

def G_Tube_l(t, Z, gamma, tau_R):
    tau_l = Z**2 * tau_R
    G_l = 1 +(gamma**2 /3) * np.exp(-t/tau_l)
    return G_l

if __name__=='__main__':
    Z1, Z2, Z3 = 100, 200, 300
    gamma = 1
    t = np.logspace(0, 6, 100)  # 時間tの刻み
    logt = np.log10(t)
    G_s = G_Tube_s(t, tau_R)
    G_l1 = G_Tube_l(t, Z1, gamma, tau_R)
    G_l2 = G_Tube_l(t, Z2, gamma, tau_R)
    G_l3 = G_Tube_l(t, Z3, gamma, tau_R)
    G1 = G_s * G_l1
    G2 = G_s * G_l2
    G3 = G_s * G_l3
    logG1 = np.log10(G1)
    logG2 = np.log10(G2)
    logG3 = np.log10(G3)

    title = r'Relaxation modulus of Tube model ($\gamma$ = {0:.1f})'.format(gamma)
    xlabel = r'$\log_{10}(t/\tau_R)$'
    ylabel = r'$\log_{10}(G(t)/G_0)$'
    savefile = './png/Tube_relaxation_modulus_gamma{0:.2f}.png'.format(gamma)

    fig = plt.figure(figsize=(8,5), tight_layout=True) 
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0, 5.5)
    ax.set_ylim(0.02, 0.5)
    ax.grid()
    ax.plot(logt, logG1, "-", color='black', label='Z = {0:.0f}'.format(Z1))
    ax.plot(logt, logG2, "-", color='black', label='Z = {0:.0f}'.format(Z2))
    ax.plot(logt, logG3, "-", color='black', label='Z = {0:.0f}'.format(Z3))
    ax.legend()
    fig.savefig(savefile, dpi=300)

    plt.show()