
"""
CooperativeGames
================
The main cooperative games functions to study cooperative games phenomena.

"""

## Elevate the main functions
from cooperativegames.measures.cooperativegames_metrics import shapley_index,\
	shapley_value, banzhaf_index, weighted_winning_coalitions,\
	weighted_worsable_coalitions

## The test functions
from cooperativegames.tests import test_measures
from cooperativegames.tests import test_measurestools
#from tests import test_plotting

## Information about package
import cooperativegames.version
#import release

## Not inform about warnings
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
warnings.simplefilter("ignore")


def test():
    test_measures.test()
    test_measurestools.test()
#    test_plotting.test()
