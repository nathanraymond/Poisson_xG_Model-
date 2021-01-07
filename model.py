import numpy as np
import pandas as pd
from itertools import combinations_with_replacement
from collections import OrderedDict

np.set_printoptions(suppress=True)

n_goals = [0, 1, 2, 3, 4, 5]

def poisson_pmf(k, lam):
    return (lam**k*np.exp(-lam))/np.math.factorial(k)

print(poisson_pmf(0,1.23))
