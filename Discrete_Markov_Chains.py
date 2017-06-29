# python3
import sys
import random
import collections
import Discrete_Probability_Spaces as dsp
import numpy as np
import itertools
import array

class discrete_markov_chain(object):

    def __init__(self, P=None):
        if P is None:
            self.P = {}
        else:
            self.P = P

    def __len__(self):
        return len(self.P)

    def states(self):
        return sorted(self.P.keys())

    def __repr__(self):
        return '\n'.join([str(x) + ":\n" + str(self.P[x]) for x in self.states()])

    def add_state(self, state, trans_prob):
        self.P[state] = trans_prob

class mcwalk(object):

    def __init__(self, MC, x=None):
        if x is not None:
            self.path = [x]
        else:
            self.path = []
        self.MC = MC

    def __len__(self):
        return len(self.path)

    def __getitem__(self, i):
        return self.path[i]

    def __repr__(self):
        return '\n'.join(str(x) for x in self.path)

    def walk(self, n):
        x = self.path[-1]
        for _ in range(n):
            x = self.MC.P[x].draw_from()
            self.path.append(x)

    def sample_dist(self):
        n = len(self)
        sample_dist = dsp.dsp()
        for x in set(self.path):
            sample_dist.add_state(x, float(self.path.count(x))/n)
        return sample_dist

def bitstrings(n):
    for w in itertools.product([0,1], repeat=n):
        yield w

def bitstring_chain(n):
    MC = discrete_markov_chain()
    for u in bitstrings(n):
        x = ''.join([str(b) for b in u])
        trans_prob = dsp.dsp()
        for i in range(n):
            v = list(u)
            v[i] = 1 - v[i]
            y = ''.join([str(b) for b in v])
            trans_prob.add_state(y, 1/n)
        MC.add_state(x, trans_prob)
    return MC

class dict_from_func(dict):

    def __init__(self, f):
        self.f = f

    def __missing__(self, key):
        self[key] = self.f(key)
        return self[key]

def simple_symm_random_walk():
    def simple_symm_random_walk_trans_probs(n):
        return dsp.dsp({n-1 : 1/2, n+1 : 1/2})
    MC = discrete_markov_chain()
    MC.P = dict_from_func(simple_symm_random_walk_trans_probs)
    return MC

class sliding_puzzle_state(object):

    def __init__(self, table):
        self.table = table
        self.m, self.n = table.shape

    def __repr__(self):
        return str(self.table)

    def zero_position(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.table[i][j] == 0:
                    return (i,j)

    def move_up(self):
        i, j = self.zero_position()
        b = np.array(self.table)
        b[i][j] = self.table[i-1][j]
        b[i-1][j] = 0
        return sliding_puzzle_state(b)

    def move_down(self):
        i, j = self.zero_position()
        b = np.array(self.table)
        b[i][j] = self.table[i+1][j]
        b[i+1][j] = 0
        return sliding_puzzle_state(b)

    def move_left(self):
        i, j = self.zero_position()
        b = np.array(self.table)
        b[i][j] = self.table[i][j-1]
        b[i][j-1] = 0
        return sliding_puzzle_state(b)

    def move_right(self):
        i, j = self.zero_position()
        b = np.array(self.table)
        b[i][j] = self.table[i][j+1]
        b[i][j+1] = 0
        return sliding_puzzle_state(b)

    def movable_positions(self):
        i, j = self.zero_position()
        N = set()
        if i > 0:
            N.add(self.move_up())
        if i < self.m - 1:
            N.add(self.move_down())
        if j > 0:
            N.add(self.move_left())
        if j < self.n - 1:
            N.add(self.move_right())
        return N

def sliding_puzzle_standard_start(m,n):
    a = np.array(range(m*n))
    a.shape = m, n
    return sliding_puzzle_state(a)

def sliding_puzzle(m,n):
    def sliding_puzzle_trans_prob(a):
        return dsp.uniform_dist(a.movable_positions())
    MC = discrete_markov_chain()
    MC.P = dict_from_func(sliding_puzzle_trans_prob)
    return MC
























