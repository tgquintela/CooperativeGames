

from scipy.spatial.distance import pdist, squareform
import numpy as np


def from_positions2weights(pos):
    """Transformation of the 1-dim measure to a weights of similarity

    Parameters
    ----------
    pos: list or np.ndarray
        the 1-dim measure.

    Returns
    -------
    weights: np.ndarray
        the square measure of relations between each one of the elements to
        the each other.

    """
    pos = np.array(pos)
    if len(pos.shape) != 1:
        pos = pos.squeeze()
    pos = pos.reshape((len(pos), 1))
    weights = pdist(pos)
    weights = 1-squareform(weights)
    return weights
