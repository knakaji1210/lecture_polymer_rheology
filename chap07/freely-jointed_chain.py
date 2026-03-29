# Freely-jointed chain (FJC) model

import numpy as np
import matplotlib.pyplot as plt

# Langevin function
def calc_Langevin(x):
    if x == 0:
        return 0
    else:
        Langevin = 1 / np.tanh(x) - 1 / x
        return Langevin

k_B = 1.38*10**(-23) # boltzmann_constant (J/K)

def reqParams():
    try:
        T = float(input('Enter absolute temperature (default = 300): '))
    except ValueError:
        T = 300
    try:
        N = int(input('Enter degree of polymerization (default = 100): '))
    except ValueError:
        N = 100
    try:
        b = float(input('Enter Kunh length (default = 0.5 nm): '))
        b = b * 10**(-9) # convert to m
    except ValueError:
        b = 0.5 * 10**(-9) # convert to m   
    return T, N, b


if __name__=='__main__':
    T, N, b = reqParams()
    y_array = np.linspace(0, 10, 100)  # y = F*b/(k_B*T)
    f_list = [ (k_B*T/b)*y * 10**12 for y in y_array] # convert to pN
    f_array = np.array(f_list)
    x_list = []
    for y in y_array:
        x = calc_Langevin(y)
        x_list.append(x)
    x_array = np.array(x_list)
    r_list = [ N*b*x * 10**9 for x in x_array] # convert to nm
    r_array = np.array(r_list)

    title = r'Freely-jointed chain ($N$ = {0}, $b$ = {1:.1f} nm, $T$ = {2:.0f} K)'.format(N, b*10**9, T)
    xlabel = r'$r$ /nm'
    ylabel = r'$f$ /pN'
    savefile = './png/freely_jointed_chain.png'

    fig = plt.figure(figsize=(8,5), tight_layout=True) 
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0, N*b*10**9)
    ax.set_ylim(0, max(f_array)*1.1)
    ax.grid()
    ax.plot(r_array, f_array, color='b')

    fig.savefig(savefile, dpi=300)

    plt.show()