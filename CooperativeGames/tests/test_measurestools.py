
"""
Module of testing the functions programed in the module in measure
cooperativegames tools.

"""

import numpy as np
from ..Measures.cooperativegames_tools import all_subsets_it,\
    winning_coalitions_it, get_critical_players, weight_coalition,\
    all_subsets, _in_set
from ..Measures.tools import from_positions2weights


def test():
    """Main function for testing power indexs of the cooperative games package.
    """

    ## From positions to weighs
    weights = from_positions2weights(np.random.random(10))
    assert(weights.shape == (10, 10))
    weights = from_positions2weights(np.random.random((10, 1)))
    assert(weights.shape == (10, 10))

    ## Set management
    set_a = [0, 1, 2]
    set_b = set_a + [5, 6]
    assert(_in_set(set_a, set_b))

    setsubsets = all_subsets(set_a)
    assert(len(setsubsets) == 2**len(set_a))
    setsubsets = all_subsets(set_b)
    assert(len(setsubsets) == 2**len(set_b))

    for subset in all_subsets_it(set_b):
        pass

    ## Combinations
    # Weigh coalition
    coalition = [0, 3, 4]
    weight_coalition(coalition, weights)

    # Get critical player
    votes = np.random.randint(0, 20, 10)
    win_v = np.around(votes.sum()*.3)
    get_critical_players(coalition, votes, win_v)

    for w_c in winning_coalitions_it(set_b, votes, win_v):
        pass
