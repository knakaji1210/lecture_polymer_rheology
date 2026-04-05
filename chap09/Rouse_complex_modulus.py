# Complex modulus of Rouse model

import numpy as np
import matplotlib.pyplot as plt

tau_R = 1.0  # Rouse緩和時間（これでスケールしたことにする）

# 変数fは周波数だがomega=2*pi*fの意味でここでは使

# short-time limit of the Rouse complex modulus
def Gstr_Rouse_s(f):
    Gstr_s = np.sqrt(np.pi/4) * np.sqrt(tau_R * f)
    return Gstr_s

def Glos_Rouse_s(f):
    Glos_s = np.sqrt(np.pi/4) * np.sqrt(tau_R * f)
    return Glos_s

def Gstr_Rouse_mode(f, p):
    Gstr_p = f**2 * tau_R**2 / (4 * p**4 + f**2 * tau_R**2)
    return Gstr_p

def Glos_Rouse_mode(f, p):
    Glos_p = 2 * f * tau_R * p**2 / (4 * p**4 + f**2 * tau_R**2)
    return Glos_p


def Gstr_Rouse(f, p_max):
    G = np.zeros_like(f)
    for p in range(1, p_max+1):
        G += Gstr_Rouse_mode(f, p)
    return G

def Glos_Rouse(f, p_max):
    G = np.zeros_like(f)
    for p in range(1, p_max+1):
        G += Glos_Rouse_mode(f, p)
    return G

def reqParams():
    try: # 描画する固有モード数
        p_max = int(input('Enter number of modes to plot (default = 10): '))
    except ValueError:
        p_max = 10
    return p_max

if __name__=='__main__':
    p_max  = reqParams()
    f = np.logspace(-3, 3, 100)  # 時間tの刻み
    logf = np.log10(f)
    Gstr_s = Gstr_Rouse_s(f)
    logGstr_s = np.log10(Gstr_s)
    Glos_s = Glos_Rouse_s(f)
    logGlos_s = np.log10(Glos_s)
    Gstr = Gstr_Rouse(f, p_max)
    logGstr = np.log10(Gstr)
    Glos = Glos_Rouse(f, p_max)
    logGlos = np.log10(Glos)
    Gstr1 = Gstr_Rouse(f, 1)
    logGstr1 = np.log10(Gstr1)
    Glos1 = Glos_Rouse(f, 1)
    logGlos1 = np.log10(Glos1)

    title1 = r'Storage modulus of Rouse model ($p_{{\max}}$ = {0:.0f})'.format(p_max)
    title2 = r'Loss modulus of Rouse model ($p_{{\max}}$ = {0:.0f})'.format(p_max)
    xlabel = r'$\log_{10}(\omega\tau_R)$'
    ylabel1 = r'$\log_{10}(G^\prime(\omega)/G_0)$'
    ylabel2 = r'$\log_{10}(G^{\prime\prime}(\omega)/G_0)$'

    savefile = './png/Rouse_complex_modulus_Pmax{0:.0f}.png'.format(p_max)

    fig = plt.figure(figsize=(8,10), tight_layout=True) 
    ax1 = fig.add_subplot(211)
    ax1.set_title(title1)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel1)
    ax1.grid()
    ax1.plot(logf, logGstr, "-", color='b', label='full Rouse')
    ax1.plot(logf, logGstr_s, ":", color='r', label='short-time limit')
    ax1.plot(logf, logGstr1, "--", color='black', label='1st mode only')
    ax1.legend()

    ax2 = fig.add_subplot(212)
    ax2.set_title(title2)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel2)
    ax2.grid()
    ax2.plot(logf, logGlos, "-", color='b', label='full Rouse')
    ax2.plot(logf, logGlos_s, ":", color='r', label='short-time limit')
    ax2.plot(logf, logGlos1, "--", color='black', label='1st mode only')
    ax2.legend()


    fig.savefig(savefile, dpi=300)

    plt.show()