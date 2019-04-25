
"""

Example
-------
colors = ['#00008B', (1, 0.5, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]
playerstags = ['A', 'B', 'C', 'D', 'E', 'F']
powers = np.array([0.5, 0.2, 0.1, 0.1, 0.05, 0.05])
fig = plotting_power(powers, playerstags, colors)

"""

import matplotlib.pyplot as plt
import numpy as np


def plotting_power(powers, playerstags, colors):
    """Plotting power.

    Parameters
    ----------
    powers: list or np.ndarray
        the list of powers for each player.
    playerstags: list
        the list of tags or names for each player.
    colors: list
        the list of colors for each player.

    Returns
    -------
    fig: matplotlib.pyplot.figure
        the figure with the horizontal bar of with the proportion of power for
        each player.

    """

    lefts = np.hstack([[0], np.cumsum(powers)])
    p = []
    fig = plt.figure()
    for i in range(powers.shape[0]):
        p.append(plt.barh(1, powers[i], height=0.2, left=lefts[i],
                          align='center', color=colors[i]))

    plt.xlabel('Power index')
    plt.title('Power Index plot')
    #plt.xticks(ind + width/2., ('G1', 'G2', 'G3', 'G4', 'G5'))
    plt.yticks([])
    plt.ylim(0.9, 1.3)
    plt.legend(tuple([pi[0] for pi in p]), tuple(playerstags))
    return fig

