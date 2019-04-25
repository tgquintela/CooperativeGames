
"""
Cooperative tools
-----------------
Complementary and auxiliary functions for the cooperativegames methods.

"""

import numpy as np
from itertools import permutations, combinations


def all_subsets_it(set_):
    """Iterator to get all the possible subsets of a set.

    Parameters
    ----------
    set_: list or np.ndarray
        the list of players.

    Returns
    -------
    comb: list
        a list of a possible combination of players between all the possible
        ones.

    """
    set_ = np.array(set_)
    n = set_.shape[0]
    for i in range(n+1):
        for comb in combinations(set_, i):
            yield list(comb)


def winning_coalitions_it(set_, votes, win_v):
    """Iterator to get all the possible winning coalitions.

    Parameters
    ----------
    set_: list or np.ndarray
        the list of players.
    votes: list or np.ndarray
        the votes of each player.
    win_v: int or float
        the winner threshold in votes.

    Returns
    -------
    coalition: list
        a winner coalition. It iteratively retrieve winner coalitions between
        all possible coalitions.

    """
    ssets = all_subsets_it(set_)
    for coalition in ssets:
        if np.sum(votes[coalition]) > win_v:
            yield coalition


def get_critical_players(coalition, votes, win_v):
    """Function to obtain all the players which converts a winning coalition in
    a loser coalition.

    Parameters
    ----------
    coalition: list
        the list of elements which defines a coalition.
    votes: list or np.ndarray
        the votes of each player.
    win_v: int or float
        the winner threshold in votes.

    Returns
    -------
    critical_players: list
        the list of players which are able to transform a winning coalition
        into a loser coalition by quiting.

    """
    coalition_v = votes[coalition]
    critical_players = np.where(win_v - np.sum(coalition_v) < coalition_v)[0]
    critical_players = list(critical_players)
    return critical_players


def weight_coalition(coalition, weights):
    """Weight coalition defined as a product of the weights of all possible
    relations.

    Parameters
    ----------
    coalition: list
        the list of elements which defines a coalition.
    weights: list or np.ndarray
        the weights between the possible pair relations between elements.

    Returns
    -------
    w_c: float
        the weights of the coalitions.

    """
    w_c = 1.
    for c in combinations(coalition, 2):
        w_c = weights[c]*w_c
    return w_c


###############################################################################
############################ AUXILIARY FUNCTIONS ##############################
###############################################################################
def all_subsets(set_):
    """All subsets possible.

    Parameters
    ----------
    set_: list or np.ndarray
        the list of possible elements to create all the combinations between
        them.

    Returns
    -------
    subsets: list
        the list of all possible subsets.

    """
    set_ = np.array(set_)
    n = set_.shape[0]
    subsets = []
    for i in range(n+1):
        subsets += [list(comb) for comb in combinations(set_, i)]
    return subsets


def _in_set(set_a, set_b):
    """If set A is in the set B.

    Parameters
    ----------
    set_a: list or np.ndarray
        the elements list of the set A.
    set_b: list or np.ndarray
        the elements list of the set B.

    Returns
    -------
    logi: boolean
        if the set A is in the set B.

    """
    return np.all([e in set_b for e in set_a])
