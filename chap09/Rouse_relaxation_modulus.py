# Relaxation modulus of Rouse model

import numpy as np
import matplotlib.pyplot as plt

tau_R = 1.0  # Rouse緩和時間（これでスケールしたことにする）

# short-time limit of the Rouse relaxation modulus
def G_Rouse_s(t):
    G_s = np.sqrt(np.pi/8) * (t/tau_R)**(-1/2)
    return G_s  

def G_Rouse_mode(t, p):
    tau_p = 1/(2*p**2) * tau_R
    G_p = np.exp(-t/tau_p)
    return G_p

def G_Rouse(t, p_max):
    G = np.zeros_like(t)
    for p in range(1, p_max+1):
        G += G_Rouse_mode(t, p)
    return G

def reqParams():
    try: # 描画する固有モード数
        p_max = int(input('Enter number of modes to plot (default = 10): '))
    except ValueError:
        p_max = 10
    return p_max

if __name__=='__main__':
    p_max  = reqParams()
    t = np.logspace(-2, 1, 100)  # 時間tの刻み
    logt = np.log10(t)
    G_s = G_Rouse_s(t)
    logG_s = np.log10(G_s)
    G = G_Rouse(t, p_max)
    logG = np.log10(G)
    G1 = G_Rouse(t, 1)
    logG1 = np.log10(G1)

    title = r'Relaxation modulus of Rouse model ($p_{{\max}}$ = {0:.0f})'.format(p_max)
    xlabel = r'$\log_{10}(-t/\tau_R)$'
    ylabel = r'$\log_{10}(G(t)/G_0)$'
    savefile = './png/Rouse_relaxation_modulus_Pmax{0:.0f}.png'.format(p_max)

    fig = plt.figure(figsize=(8,5), tight_layout=True) 
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid()
    ax.plot(logt, logG, "-", color='b', label='full Rouse')
    ax.plot(logt, logG_s, ":", color='r', label='short-time limit')
    ax.plot(logt, logG1, "--", color='black', label='1st mode only')
    ax.legend()
    fig.savefig(savefile, dpi=300)

    plt.show()