# binodal distribution

import math
import numpy as np
import matplotlib.pyplot as plt

# permutations with identical items
def calc_PermIdenticalItem(totalStep, num):                           
    weight = math.factorial(totalStep) / (math.factorial(num) * math.factorial(totalStep - num))
    return weight

def reqParams():
    try:
        totalStep = int(input('Enter total number of steps (default = 100): '))
    except ValueError:
        totalStep = 100
    return totalStep


if __name__=='__main__':
    totalStep = reqParams()
    stepNum = np.linspace(0, totalStep, totalStep+1)

    try:
        select = int(input('Selection (W_N(n): 0, P_N(n): 1): '))
    except ValueError:
        select = 0
    
    if select == 0:
        # binodal distribution(weight)
        weight_list = []
        for n in stepNum:
            weight = calc_PermIdenticalItem(totalStep, int(n))
            weight_list.append(weight)
        weight_array = np.array(weight_list)
        x = stepNum
        y = weight_array
        title = r'binodal distribution (weight) (total step = {0})'.format(totalStep)
        xlabel = r'$n$'
        ylabel = r'$W_{{{N}}}$($n$)'
        savefile = './png/binodal_distribution_weight.png'
    elif select == 1:
        # binodal distribution(probability)
        prob_list = []
        for n in stepNum:
            weight = calc_PermIdenticalItem(totalStep, int(n))
            prob = weight / 2**totalStep
            prob_list.append(prob)
        prob_array = np.array(prob_list)
        x = stepNum
        y = prob_array
        title = r'binodal distribution (probability) (total step = {0})'.format(totalStep)
        xlabel = r'$n$'
        ylabel = r'$P_{{{N}}}$($n$)'
        savefile = './png/binodal_distribution_probability.png'
    else:
        pass


    fig = plt.figure(figsize=(8,5), tight_layout=True)
    xlim = np.sqrt(totalStep)*3
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(totalStep/2-xlim, totalStep/2+xlim)
    ax.set_ylim(0, max(y)*1.1)
    ax.grid()
    ax.bar(x, y, color='b', width=xlim/100, align='center')
    ax.scatter(x, y, color='b', s=xlim/2)

    fig.savefig(savefile, dpi=300)

    plt.show()