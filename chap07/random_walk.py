# random walk (1d)

import math
import numpy as np
import matplotlib.pyplot as plt

# permutations with identical items
def calc_PermIdenticalItem(totalStep, num):                           
    weight = math.factorial(totalStep) / (math.factorial(num) * math.factorial(totalStep - num))
    return weight

# Gaussian distribution
def calc_Gaussian(totalStep, x):
    sigma = np.sqrt(totalStep)
    prob = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * (x / sigma)**2)
    return prob

def reqParams():
    try:
        totalStep = int(input('Enter total number of steps (default = 100): '))
    except ValueError:
        totalStep = 100
    return totalStep


if __name__=='__main__':
    a = 1
    totalStep = reqParams()
    stepNum = np.linspace(0, totalStep, totalStep+1)
    x_list = [ a*(2*n - totalStep) for n in stepNum]
    x_array = np.array(x_list)

    try:
        select = int(input('Selection (discrete: 0, approximation: 1, continuous: 2): '))
    except ValueError:
        select = 0
    
    if select == 0:
        # random walk (discrete)
        prob_list = []
        for n in stepNum:
            weight = calc_PermIdenticalItem(totalStep, int(n))
            prob = weight / 2**totalStep /2
            prob_list.append(prob)
        prob_array = np.array(prob_list)
        x = x_array
        y = prob_array
        title = r'random walk (discrete) (total step = {0})'.format(totalStep)
        xlabel = r'$x$'
        ylabel = r'$F_{{{N}}}$($x$)'
        savefile = './png/random_walk_discrete.png'
    elif select == 1:
        # random walk (approximation by Gaussian function)
        prob_list = []
        for x in x_array:
            prob = calc_Gaussian(totalStep, x)
            prob_list.append(prob)
        prob_array = np.array(prob_list)
        x = x_array
        y = prob_array
        title = r'random walk (approximation) (total step = {0})'.format(totalStep)
        xlabel = r'$x$'
        ylabel = r'$F_{{{N}}}$($x$)'
        savefile = './png/random_walk_approximation.png'
    elif select == 2:
        # random walk (continuous)
        prob_list = []
        for x in x_array:
            prob = calc_Gaussian(totalStep, x)
            prob_list.append(prob)
        prob_array = np.array(prob_list)
        x = x_array
        y = prob_array
        title = r'random walk (continuous) (total step = {0})'.format(totalStep)
        xlabel = r'$x$'
        ylabel = r'$F$($x$)'
        savefile = './png/random_walk_continuous.png'

    fig = plt.figure(figsize=(8,5), tight_layout=True)
    xlim = np.sqrt(totalStep)*6
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(-xlim, xlim)
    ax.set_ylim(0, max(y)*1.1)
    ax.grid()
    if select == 0:
        ax.bar(x, y, color='b', width=xlim/100, align='center')
        ax.scatter(x, y, color='b', s=xlim/2)
    elif select == 1:
        ax.plot(x, y, color='b', linewidth=2)
        ax.scatter(x, y, color='b', s=xlim/2)
    elif select == 2:
        ax.plot(x, y, color='b', linewidth=2)

    fig.savefig(savefile, dpi=300)

    plt.show()