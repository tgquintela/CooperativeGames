
"""
TODO
----
ignore zeros
"""

import pandas as pd
import numpy as np

from cooperativegames import shapley_index, banzhaf_index


def parse_csv(path, win_thrs, outpath=None):
    aux = pd.read_csv(path, sep=';', index_col=0).replace({'-': 0})
    g_names, g_parties = list(aux.index), list(aux.columns)
    g_res = aux.as_matrix().astype(float).astype(int)
    g_meas, n_parties = len(g_names)*2*len(win_thrs), len(g_parties)
    powers, pw_names = np.zeros((g_meas, n_parties)).astype(float), []
    for i in range(len(g_names)):
        print i
        for j in range(len(win_thrs)):
            #powers[4*i+2*j, :] = shapley_index(g_res[i, :], win_thrs[j])
            powers[4*i+2*j, :] = np.zeros(len(g_parties))
            powers[4*i+2*j+1, :] = banzhaf_index(g_res[i, :], win_thrs[j])
            pw_names.append('shapley_'+str(win_thrs[j])+'//'+g_names[i])
            pw_names.append('banzhaf_'+str(win_thrs[j])+'//'+g_names[i])
    res_mea = pd.DataFrame(powers, columns=g_parties, index=pw_names)
    if outpath is not None:
        res_mea.to_csv(outpath, sep=';')
    return res_mea




