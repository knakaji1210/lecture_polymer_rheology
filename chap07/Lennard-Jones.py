# Lennard-Jones　potential & force 

import numpy as np
import matplotlib.pyplot as plt

def calc_LJP(sigma, epsilon, r):                            # Lennard-Jones potential
    funcLJP = 4*epsilon*((sigma/r)**12-(sigma/r)**6)   
    return funcLJP

def calc_LJF(sigma, epsilon, r):                            # Lennard-Jones force   
    funcLJF = 4*(epsilon/sigma)*(12*(sigma/r)**13-6*(sigma/r)**7)   
    return funcLJF

def reqParams():
    try:
        sigma = float(input('Enter size parameter, sigma (default = 0.34 nm): '))
    except ValueError:
        sigma = 0.34
    try:
        epsilon = float(input('Enter energy parameter, epsilon (default = 10^(-18) J): '))
    except ValueError:
        epsilon = 10**(-18)
    return sigma, epsilon

if __name__=='__main__':
    # Lennard-Jones　potential & force 
    atomic_distance = np.linspace(0.1, 1.0, 200)    # range of atomic distance (nm)
    sigma, epsilon = reqParams()
    bond_length = sigma*2**(1/6)                  # bond length (nm)
    param_text = r'($\sigma$ = {0:.2f} nm, $\epsilon$ = {1:.2f} x $10^{{-18}}$ J)'.format(sigma, epsilon*10**18)
    
    x = atomic_distance
    x_label = r'atomic distance, $r$ /nm'
    y1 = calc_LJP(sigma, epsilon, x)
    y1_label = r'$U$($r$) /J'
    label1 = r'Lennard-Jones potential ' + param_text
    y2 = calc_LJF(sigma, epsilon, x)
    y2_label = r'$F$($r$) /N'
    label2 = r'Lennard-Jones force ' + param_text

    # drawing graphs
    fig = plt.figure(figsize=(8,10), tight_layout=True)
    ax1 = fig.add_subplot(211)
    ax1.set_title(label1)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label)
    ax1.set_xlim(0, 1.0)
    ax1.set_ylim(-1.5*epsilon, 2.0*epsilon)
    ax1.grid()
    ax1.plot(x, y1, c='b', label=label1)
    ax1.hlines(0, 0, 1, colors='k', linestyles='dashed')
    ax1.vlines(bond_length, -1.5*epsilon, 2.0*epsilon, colors='k', linestyles='dashed')
    ax2 = fig.add_subplot(212)
    ax2.set_title(label2)
    ax2.set_xlabel(x_label)
    ax2.set_ylabel(y2_label)
    ax2.set_xlim(0, 1.0)
    ax2.set_ylim(-15*epsilon, 20.0*epsilon)
    ax2.grid()
    ax2.plot(x, y2, c='r', label=label2)
    ax2.hlines(0, 0, 1, colors='k', linestyles='dashed')
    ax2.vlines(bond_length, -15*epsilon, 20*epsilon, colors='k', linestyles='dashed')

    savefile = './png/Lennard-Jones.png'
    fig.savefig(savefile, dpi=300)

    plt.show()