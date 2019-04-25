
"""
Testing plotting tools
----------------------
Module which contains the tests for the plotting utitilies.

"""

import numpy as np
from cooperativegames.plotting_tools.plotting import plotting_power


def test():
    colors = ['#00008B', (1, 0.5, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]
    playerstags = ['A', 'B', 'C', 'D', 'E', 'F']
    powers = np.array([0.5, 0.2, 0.1, 0.1, 0.05, 0.05])
    fig = plotting_power(powers, playerstags, colors)
