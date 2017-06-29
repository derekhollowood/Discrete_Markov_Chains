# Discrete_Markov_Chains
Python class for discrete Markov chains.

## Examples
### User specified Markov chain
```ipython3
In [1]: import Discrete_Markov_Chains as dmc

In [2]: MC = dmc.bitstring_chain(3)

In [3]: walk = dmc.mcwalk(MC, '000')

In [4]: walk.walk(19)

In [5]: walk
Out[5]: 
000
001
101
111
101
111
101
111
101
001
101
001
101
111
110
111
011
001
101
111

In [6]: walk.sample_dist()
Out[6]: 
001 : 0.2
000 : 0.05
011 : 0.05
101 : 0.35
110 : 0.05
111 : 0.3

