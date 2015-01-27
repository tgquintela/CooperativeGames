
__author__ = 'T. G. Quintela (tgq.spm@gmail.com)'

""" Module which groups functions useful for the study of cooperative games.

TODO:
----
shapley_value
assimetric shapley Index
"""

import numpy as np
from itertools import permutations, combinations
from collections import Counter
import math


def shapley_index(distrib_repr, win_thr=0.5):
    """

    References
    ----------
    .. [1] Shapley, L. S.; Shubik, M. (1954). "A Method for Evaluating the
    Distribution of Power in a Committee System". American Political Science
    Review 48 (3): 787-792. doi:10.2307/1951053

    TODO
    ----
    Hu, X. (2006). "An Asymmetric Shapley-Shubik Power Index". International
    Journal of Game Theory 34 (2): 229-240. doi:10.1007/s00182-006-0011-z.

    """
    n = distrib_repr.shape[0]
    n_v = np.sum(distrib_repr)
    win_v = n_v*win_thr
    p = math.factorial(n)

    cum = []
    perm = permutations(range(n), n)
    for per in perm:
        idx = np.where(np.cumsum(distrib_repr[list(per)]) >= win_v)[0][0]
        cum.append(per[idx])
    c = Counter(cum)
    shapley_ind = np.array(c.values())/float(p)

    return shapley_ind


def banzhaf_index(distrib_repr, win_thr=0.5):
    """

    References
    ----------
    .. [1] Banzhaf, John F. (1965), "Weighted voting doesn't work: A
    mathematical analysis", Rutgers Law Review 19 (2): 317-343

    """

    # Initalization of variables
    n = distrib_repr.shape[0]
    n_v = np.sum(distrib_repr)
    win_v = n_v*win_thr

    # Compute subsets and wining subsets
    subsets = all_subsets(range(n))
    win_subsets = [subsets[i] for i in range(len(subsets))
                   if np.sum(distrib_repr[subsets[i]]) > win_v]

    # Obtaining swing voters
    swing_voters = []
    for wsset in win_subsets:
        aux = []
        for e in wsset:
            if np.sum(distrib_repr[wsset]) - distrib_repr[e] <= win_v:
                aux.append(e)
        swing_voters.append(aux)

    # Count swing voters
    aux = []
    for e in swing_voters:
        aux += e
    c = Counter(aux)
    nc = len(aux)
    # Computing index
    banzhaf_ind = np.zeros(distrib_repr.shape)
    banzhaf_ind[c.keys()] = np.array(c.values())/float(nc)

    return banzhaf_ind


def shapley_value(set_, value_func=lambda x: 1):
    """

    References
    ----------
    .. [1] Lloyd S. Shapley. "A Value for n-person Games". In Contributions to
    the Theory of Games, volume II, by H.W. Kuhn and A.W. Tucker, editors.
    Annals of Mathematical Studies v. 28, pp. 307-317. Princeton University
    Press, 1953.
    """

    # Initialization
    set_ = np.array(set_)
    n = set_.shape[0]
    idx = np.array(range(n))
    except_idx = [[j for j in idx if j != i] for i in idx]

    # Computation of the values
    phis = []
    for i in idx:
        ssets = all_subsets(except_idx[i])
        ssets = [] + ssets
        phi = 0
        for j in range(len(ssets)):
            l = len(ssets[j])
            cte = math.factorial(l) * math.factorial(n-l-1)
            cte = np.abs(cte / float(math.factorial(n)))
            idsx1 = list(np.sort(ssets[j]+[i]))
            idsx2 = list(np.sort(ssets[j]))
            phi += cte * (value_func(set_[idsx1])-value_func(set_[idsx2]))
        phis.append(phi)

    shap_values = np.array(phis)
    return shap_values


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
