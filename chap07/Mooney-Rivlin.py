# Mooney-Rivlin model for hyperelasticity

import numpy as np
import matplotlib.pyplot as plt

# neo-Hookean model
def calc_NeoHookeanSrain(x):
    neoHookean = x - 1/x**2
    return neoHookean

# Mooney-Rivlin model
def calc_MooneyRivlin(x, C1, C2):
    mooneyRivlin = (2*C1 + 2*C2/x) * calc_NeoHookeanSrain(x)
    return mooneyRivlin

def reqParams():
    try:
        C1 = float(input('Enter C1 parameter (default = 0.2 MPa): '))
    except ValueError:
        C1 = 0.2
    try:
        C2 = float(input('Enter C2 parameter (default = 0.1 MPa): '))
    except ValueError:
        C2 = 0.1
    return C1, C2


if __name__=='__main__':
    C1, C2 = reqParams()
    E = 6 * C1  # Young's modulus
    Em = 3*(2*C1 + 2*C2)
    lambda_array = np.linspace(1, 2, 100)  # stretch ratio, defautでは1から2まで、MR plotでは1から10までに変更する
    inv_lambda_array = 1 / lambda_array
    sigma_neoHookean_list = []
    sigma_mooneyRivlin_list = []
    for l in lambda_array:
        sigma_neoHookean = (Em/3) * calc_NeoHookeanSrain(l)
        sigma_mooneyRivlin = calc_MooneyRivlin(l, C1, C2)
        sigma_neoHookean_list.append(sigma_neoHookean)
        sigma_mooneyRivlin_list.append(sigma_mooneyRivlin)
    sigma_neoHookean_array = np.array(sigma_neoHookean_list)
    sigma_mooneyRivlin_array = np.array(sigma_mooneyRivlin_list)
    scaled_sigma_mooneyRivlin_array = np.divide(sigma_mooneyRivlin_array, sigma_neoHookean_array, out=np.ones_like(sigma_mooneyRivlin_array), where=sigma_neoHookean_array!=0)

    try:
        select = int(input('Selection (stress-strain curve: 0, Mooney-Rivlin plot: 1): '))
    except ValueError:
        select = 0

    fig = plt.figure(figsize=(8,5), tight_layout=True) 
    ax = fig.add_subplot(111)

    if select == 0:
        title = r'Mooney-Rivlin model for Hyperelasticity ($E$ = {0:.2f} MPa, $C_{{1}}$ = {1:.2f} MPa, $C_{{2}}$ = {2:.2f} MPa)'.format(Em, C1, C2)
        xlabel = r'$\lambda$ /'
        ylabel = r'$\sigma$ /MPa'
        xlim = max(lambda_array)
        ylim = max(sigma_neoHookean_array)*1.1
        savefile = './png/Mooney-Rivlin (stress-strain).png'
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_xlim(1, xlim)
        ax.set_ylim(0, ylim)    
        ax.plot(lambda_array, sigma_neoHookean_array, "--", color='r', label='neo-Hookean')
        ax.plot(lambda_array, sigma_mooneyRivlin_array, "-", color='b', label='Mooney-Rivlin')
    elif select == 1:
        title = r'Mooney-Rivlin plot ($C_{{1}}$ = {0:.2f} MPa, $C_{{2}}$ = {1:.2f} MPa)'.format(C1, C2)
        xlabel = r'1/$\lambda$ /'
        ylabel = r'scaled $\sigma$ /MPa'
        ylim = 2 * max(scaled_sigma_mooneyRivlin_array)
        savefile = './png/Mooney-Rivlin_plot.png'
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_xlim(0.0, 1.1)
        ax.set_ylim(0, ylim)
        ax.plot(inv_lambda_array, scaled_sigma_mooneyRivlin_array, "-", color='b', label='Mooney-Rivlin')

    else:
        pass

    ax.grid()
    ax.legend()
    fig.savefig(savefile, dpi=300)

    plt.show()