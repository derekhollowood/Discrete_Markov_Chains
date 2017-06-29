# python3
import sys
import random
import itertools
import numpy as np

class dsp(object):

    def __init__(self, pmf=None):
        if pmf is None:
            self.pmf = {}
        else:
            self.pmf = pmf

    def __len__(self):
        return len(self.pmf)

    def states(self):
        return sorted(self.pmf.keys())

    def __repr__(self):
        return '\n'.join([str(state)+" : "+str(self.pmf[state]) for state in self.pmf])

    def add_state(self, state, prob):
        self.pmf[state] = prob

    def draw_from(self):
        U = random.random()
        p = 0
        for state in self.pmf:
            p += self.pmf[state]
            if p > U:
                return(state)
        return None

    def prob(self, event):
        return np.sum([self.pmf(state) for state in self.states if event(state)])

    def iid_sampling(self, n):
        S = dsp()
        for w in itertools.product(self.states()):
            p = np.prod(np.array(self.pmf[x] for x in w))
            S.add_state(w, p)

def uniform_dist(S):
    return dsp({s : 1/len(S) for s in list(S)})

def coin_toss():
    return dsp({'H' : 1/2, 'T' : 1/2})

def cointosses(n):
    S = dsp()
    for w in itertools.product(self.states()):
        p = np.prod(np.array(self.pmf[c] for c in w))
        x = ''.join(c for c in w)
        S.add_state(x, p)






























