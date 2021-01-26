import numpy as np
import pandas as pd
from itertools import combinations_with_replacement
from collections import OrderedDict

np.set_printoptions(suppress=True)

n_goals = [0, 1, 2, 3, 4, 5]

np.set_printoptions(suppress=True)


class PoissonModel():
	def __init__(self, inputdict, probability):
		self.lam_home = float(inputdict["home"])
		self.lam_away = float(inputdict["away"])
		self.probability = probability
		self.n_goals = [0, 1, 2, 3, 4, 5]

	def poisson_pmf_goals_home(self):
	    probs = []
	    for k in self.n_goals:
	        probs.append((self.lam_home**k*np.exp(-self.lam_home))/np.math.factorial(k))
	    return (np.array([probs,]*6)).T

	def poisson_pmf_goals_away(self):
	    probs = []
	    for k in self.n_goals:
	        probs.append((self.lam_away**k*np.exp(-self.lam_away))/np.math.factorial(k))
	    return np.array([probs,]*6)

	def get_probabilty_df(self):
		prob = self.poisson_pmf_goals_home()*self.poisson_pmf_goals_away()
		return pd.DataFrame(prob, columns = ['0','1','2','3','4','5'], index = ['0','1','2','3','4','5'])

	def get_match_probability(self):
		combs = list(OrderedDict.fromkeys(list(combinations_with_replacement(['0','1','2','3','4','5','4','3','2','1','0'], 2))))
		if (self.probability).lower() == 'home':
			return sum((self.get_probabilty_df()).loc[combs[i]] for i in range (0, len(combs)) if combs[i][0] > combs[i][1])
		elif (self.probability).lower() == 'away':
			return sum((self.get_probabilty_df()).loc[combs[i]] for i in range (0, len(combs)) if combs[i][0] < combs[i][1])
		elif (self.probability).lower() == 'draw':
			return sum((self.get_probabilty_df()).loc[combs[i]] for i in range (0, len(combs)) if combs[i][0] == combs[i][1])
		elif (self.probability).lower() == 'all':
			return {"home": sum((self.get_probabilty_df()).loc[combs[i]] for i in range (0, len(combs)) if combs[i][0] > combs[i][1]), "draw": sum((self.get_probabilty_df()).loc[combs[i]] for i in range (0, len(combs)) if combs[i][0] == combs[i][1]), "away": sum((self.get_probabilty_df()).loc[combs[i]] for i in range (0, len(combs)) if combs[i][0] < combs[i][1])}
		

