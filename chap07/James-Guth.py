# non-Gaussian model by James Guth (1943)

import numpy as np
import matplotlib.pyplot as plt

# Pade approximation to the inverse Langevin function
def calc_Pade(x):
    Pade = 3*x*(35 - 12*x**2)/(35 - 33*x**2)
    return Pade

# neo-Hookean model
def calc_NeoHookean(x):
    neoHookean = x - 1/x**2
    return neoHookean

def reqParams():
    try:
        N_c = int(input('Enter degree of polymerization between crosslinks (default = 60): '))
    except ValueError:
        N_c = 60
    try:
        E = float(input('Enter Young\'s modulus (default = 1.0 MPa): '))
    except ValueError:
        E = 1.0
    return N_c, E


if __name__=='__main__':
    N_c, E = reqParams()
    lambda_m = np.sqrt(N_c) # maximum stretch ratio
    lambda_array = np.linspace(1, 7, 100)  # stretch ratio
    x1_list = [ l / lambda_m for l in lambda_array]
    x2_list = [ (1/lambda_m)*np.sqrt(l) for l in lambda_array]
    sigma1_list = []
    sigma2_list = []
    for i in range(len(lambda_array)):
        s1 = calc_Pade(x1_list[i])
        s2 = calc_Pade(x2_list[i])
        sigma1 = (E/3) * (1/3) * lambda_m * (s1 - (1/lambda_array[i]**(3/2))*s2)
        sigma1_list.append(sigma1)
        sigma2 = (E/3) * calc_NeoHookean(lambda_array[i])
        sigma2_list.append(sigma2)
    sigma1_array = np.array(sigma1_list)
    sigma2_array = np.array(sigma2_list)

    title = r'non-Gaussian model by James & Guth ($E$ = {0:.1f} MPa, $N_{{c}}$ = {1:.0f})'.format(E, N_c)
    xlabel = r'$\lambda$ /'
    ylabel = r'$\sigma$ /MPa'
    savefile = './png/James-Guth.png'

    fig = plt.figure(figsize=(8,5), tight_layout=True) 
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid()
    ax.plot(lambda_array, sigma1_array, "-", color='r', label='non-Gaussian')
    ax.plot(lambda_array, sigma2_array, "--", color='b', label='neo-Hookean')
    ax.legend()
    fig.savefig(savefile, dpi=300)

    plt.show()