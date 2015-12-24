
"""
Cooperative tools
-----------------
Complementary and auxiliary functions for the cooperativegames methods.

"""

import numpy as np
from itertools import permutations, combinations


def all_subsets_it(set_):
    """Iterator to get all the possible subsets of a set.
    """
    set_ = np.array(set_)
    n = set_.shape[0]
    subsets = []
    for i in range(n+1):
        for comb in combinations(set_, i):
            yield list(comb)


def winning_coalitions_it(set_, votes, win_v):
    """Iterator to get all the possible winning coalitions.
    """
    ssets = all_subsets_it(set_)
    for coalition in ssets:
        if np.sum(votes[coalition]) > win_v:
            yield coalition


def get_critical_players(coalition, votes, win_v):
    """Function to obtain all the players which converts a winning coalition in
    a loser coalition.
    """
    coalition_v = votes[coalition]
    critical_parties = list(np.where(win_v - np.sum(coalition_v) < coalition_v)[0])
    return critical_parties


def weight_coalition(coalition, weights):
    """Weight coalition
    """
    w_c = 1.
    for c in combinations(coalition, 2):
        w_c = weights[c]*w_c
    return w_c


###############################################################################
############################ AUXILIARY FUNCTIONS ##############################
###############################################################################
def all_subsets(set_):
    set_ = np.array(set_)
    n = set_.shape[0]
    subsets = []
    for i in range(n+1):
        subsets += [list(comb) for comb in combinations(set_, i)]
    return subsets


def _in_set(set_a, set_b):
    return np.all([e in set_b for e in set_a])

