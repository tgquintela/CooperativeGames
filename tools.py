

from scipy.spatial.distance import pdist, squareform
import numpy as np


def from_positions2weights(pos):
    if len(pos.shape) == 1:
        pos = np.vstack([pos, np.zeros(pos.shape)]).T
    else:
        pos = pos.T
    weights = pdist(pos)
    weights = 1-squareform(weights)
    return weights


