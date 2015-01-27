
__author__ = 'To\xc3\xb1o G. Quintela (tgq.spm@gmail.com)'

"""Module of testing the functions programed in the module cooperativegames.
"""

import numpy as np
from cooperativegames import shapley_index, banzhaf_index, shapley_value


def test_CooperativeGames():
    """Main function for testing power indexs of the cooperative games package.
    """

    def test1_shapley_value(funct):
        """Glove game:
        Consider a simplified description of a business. An owner, o, provides
        crucial capital in the sense that without him no gains can be obtained.
        There are k workers w1,...,wk, each of whom contributes an amount p to
        the total profit. So N = {o, w1,...,wk} and v(S) = 0 if o is not a
        member of S and v(S) = mp if S contains the owner and m workers.
        Computing the Shapley value for this coalition game leads to a value of
        kp/2 for the owner and p/2 for each worker.

        (http://en.wikipedia.org/wiki/Shapley_value)
        """
        sh_v1 = shapley_value(np.array(range(3)), funct)
        result = np.array([1./6, 1./6, 2./3])

        print("Testing Shapley value with the globe game.")
        np.testing.assert_array_almost_equal(sh_v1, result)
        print("Test passed.")
        print("-------------------------------------------------------")

    def test1_banzhaf_index(funct):
        """Voting game from Game Theory and Strategy by Phillip D. Straffin:
        [6; 4, 3, 2, 1]
        The numbers in the brackets mean a measure requires 6 votes to pass,
        and voter A can cast four votes, B three votes, C two, and D one. The
        winning groups, with parenthesis swing voters, are as follows:

        (AB), (AC), (A)BC, (AB)D, (AC)D, (BCD), ABCD

        There are 12 total swing votes, so by the Banzhaf inex is:
        A = 5/12, B = 3/12, C = 3/12, D = 1/12

        (http://en.wikipedia.org/wiki/Banzhaf_power_index)
        """

        bzf_ind = banzhaf_index(*funct())
        result = np.array([5./12, 3./12, 3./12, 1./12])

        print("Testing Banzhaf index with Straffin voting game.")
        np.testing.assert_array_almost_equal(bzf_ind, result, 3)
        print("Test passed.")
        print("-------------------------------------------------------")

    def test2_banzhaf_index(funct):
        """US voting 1 wikipedia:
        Consider the U.S. Electoral College. Each state has more or less power
        than the next state. There are a total of 538 electoral votes. A
        majority vote is considered 270 votes. The Banzhaf power index would be
        a mathematical representation of how likely a single state would be
        able to swing the vote. For a state such as California, which is
        allocated 55 electoral votes, they would be more likely to swing the
        vote than a state such as Montana, which only has 3 electoral votes.

        The United States is having a presidential election between a
        Republican and a Democrat. For simplicity, suppose that only three
        states are participating: California (55 electoral votes), Texas (34
        electoral votes), and New York (31 electoral votes).

        Results are all with 1/3.

        (http://en.wikipedia.org/wiki/Banzhaf_power_index)
        """

        bzf_ind = banzhaf_index(*funct())
        result = np.array([1./3, 1./3, 1./3])

        print("Testing Banzhaf index with US voting game 1.")
        np.testing.assert_array_almost_equal(bzf_ind, result, 3)
        print("Test passed.")
        print("-------------------------------------------------------")

    def test3_banzhaf_index(funct):
        """US voting 2 wikipedia:
        Consider the U.S. Electoral College. Each state has more or less power
        than the next state. There are a total of 538 electoral votes. A
        majority vote is considered 270 votes. The Banzhaf power index would be
        a mathematical representation of how likely a single state would be
        able to swing the vote. For a state such as California, which is
        allocated 55 electoral votes, they would be more likely to swing the
        vote than a state such as Montana, which only has 3 electoral votes.

        The United States is having a presidential election between a
        Republican and a Democrat. For simplicity, suppose that only three
        states are participating: California (55 electoral votes), Texas (34
        electoral votes), and Ohio (20 electoral votes).

        Results are [1, 0, 0].

        (http://en.wikipedia.org/wiki/Banzhaf_power_index)
        """

        bzf_ind = banzhaf_index(*funct())
        result = np.array([1., 0, 0])

        print("Testing Banzhaf index with US voting game 2.")
        np.testing.assert_array_almost_equal(bzf_ind, result, 3)
        print("Test passed.")
        print("-------------------------------------------------------")

    def test4_banzhaf_index(funct):
        """Cartel game
        Five companies (A, B, C, D, E) sign an agreement for the creation of a
        monopoly. The size of the market is X = 54 millions units per year
        (i.e. petroleum barrels) for a monopoly. The maximum production
        capacity of these companies is A = 44, B = 32, C = 20, D = 8 and E = 4
        millions of units per year. Therefore, there is a set of coalitions
        able to provide the 54 millions of units necessary for the monopoly,
        and a set of coalitions unable to provide that number. In each of the
        sufficient coalitions we may have necessary members (for the coalition
        to provide the required production) and unnecessary members (underlined
        in the table below). Even when one of these unnecessary members goes
        out of the sufficient coalition that coalition is able to provide the
        required production. However, when one necessary member leaves, the
        sufficient coalition becomes insufficient.
        The monopoly's profit to be distributed among the coalition's members
        is 100 millions of dollars per year.

        A is necessary in 38,5% of the total cases, B in 23.1%, C in 23.1%, D
        in 7.7% and E in 7.7% (these are the Banshaf indexes for each company).
        """

        bzf_ind = banzhaf_index(*funct())
        result = np.array([.385, .231, .231, .077, .077])

        print("Testing Banzhaf index with Cartel game.")
        np.testing.assert_array_almost_equal(bzf_ind, result, 3)
        print("Test passed.")
        print("-------------------------------------------------------")

    def test5_banzhaf_index(funct):
        """EEC 1958-1972:
        (https://en.wikipedia.org/wiki/Voting_in_the_Council_of_the_European_
        Union#Treaty_of_Rome_.281958.E2.80.931973.29)
        """

        bzf_ind = banzhaf_index(*funct())
        result = np.array([5/21., 5/21., 5/21., 3/21., 3/21., 0])

        print("Testing Banzhaf index with EEC voting.")
        np.testing.assert_array_almost_equal(bzf_ind, result, 3)
        print("Test passed.")
        print("-------------------------------------------------------")

    def test1_shapley_shubik(funct):
        """Example from the wikipedia:

        (http://en.wikipedia.org/wiki/Shapley%E2%80%93Shubik_power_index)
        """

        sh_sh_ind = shapley_index(*funct())
        result = np.array([1/2., 1/6., 1/6., 1/6.])

        print("Testing Shapley-Shubick index with example.")
        np.testing.assert_array_almost_equal(sh_sh_ind, result, 3)
        print("Test passed.")
        print("-------------------------------------------------------")

    @test1_shapley_value
    def f_globe_game(set_):
        set_ = list(set_)
        if set_ in [[0, 2], [1, 2], [0, 1, 2]]:
            return 1
        else:
            return 0

    @test1_banzhaf_index
    def f_voting_test1():
        distrib_repr = np.array([4, 3, 2, 1])
        win_thr = 0.5
        return [distrib_repr, win_thr]

    @test2_banzhaf_index
    def f_usvoting1_test():
        distrib_repr = np.array([55, 34, 31])
        win_thr = 0.5
        return [distrib_repr, win_thr]

    @test3_banzhaf_index
    def f_usvoting2_test():
        distrib_repr = np.array([55, 34, 20])
        win_thr = 0.5
        return [distrib_repr, win_thr]

    @test4_banzhaf_index
    def f_cartel_test():
        distrib_repr = np.array([44, 32, 20, 8, 4])
        win_thr = float(54.)/np.sum(distrib_repr)
        return [distrib_repr, win_thr]

    @test5_banzhaf_index
    def f_eu1_test():
        "EEC 1958-1972"
        distrib_repr = np.array([4, 4, 4, 2, 2, 1])
        win_thr = 11.9/np.sum(distrib_repr)
        return [distrib_repr, win_thr]

    @test1_shapley_shubik
    def f_ex_test():
        distrib_repr = np.array([3, 2, 1, 1])
        win_thr = .5
        return [distrib_repr, win_thr]
