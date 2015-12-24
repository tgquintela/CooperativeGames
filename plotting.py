
"""

colors = ['#00008B', (1, 0.5, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]
"""

import matplotlib.pyplot as plt
import numpy as np


def plotting_power(powers, playerstags, colors):

    lefts = np.hstack([[0], np.cumsum(powers)])
    p = []
    fig = plt.figure()
    for i in range(powers.shape[0]):
        p.append(plt.barh(1, powers[i], height=0.2, left=lefts[i], align='center', color=colors[i]))

    plt.xlabel('Power index')
    plt.title('Power Index plot')
    #plt.xticks(ind + width/2., ('G1', 'G2', 'G3', 'G4', 'G5'))
    plt.yticks([])
    plt.ylim(0.9, 1.3)
    plt.legend(tuple([pi[0] for pi in p]), tuple(playerstags))
    return fig

