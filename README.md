
[![Build Status](https://travis-ci.org/tgquintela/CooperativeGames.svg?branch=master)](https://travis-ci.org/tgquintela/CooperativeGames)
[![Coverage Status](https://coveralls.io/repos/github/tgquintela/CooperativeGames/badge.svg?branch=master)](https://coveralls.io/github/tgquintela/CooperativeGames?branch=master)
# CooperativeGames
Some measure useful for cooperative games. 
In this first version it contains:

* [Shapley value](http://en.wikipedia.org/wiki/Shapley_value)
* [Shapley–Shubik power index](http://en.wikipedia.org/wiki/Shapley%E2%80%93Shubik_power_index)
* [Banzhaf power index](http://en.wikipedia.org/wiki/Banzhaf_power_index)


# Tutorial

The easy way to use this functions are:

* Shapley value
```python
from Cooperativegames import shapley_value

entities = np.array(range(3))
funct = lambda x: 1 if list(x) in [[0, 2], [1, 2], [0, 1, 2]] else 0
sh_v1 = shapley_value(entities, funct)

```

* Shapley-Shubik power index
```python
from Cooperativegames import shapley_index

distrib_repr = np.array([3, 2, 1, 1])
win_thr = 0.5
sh_sh_ind = shapley_index(distrib_repr, win_thr)

```

* Banzhaf power index
```python
from Cooperativegames import banzhaf_index

distrib_repr = np.array([4, 3, 2, 1])
win_thr = 0.5
bzf_ind = banzhaf_index(distrib_repr, win_thr)

```


# Testing the module
It is provide a testing module called test.py. It runs only with the importation.

```python

import CooperativeGames
CooperativeGames.test()

```
or it could be done also with nosetests of [nose](http://nose.readthedocs.org/en/latest/index.html),
```bash

nosetests
```

# TODO

* plots and visualizations
* simulations
* obtain data
