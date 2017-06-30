# Discrete_Markov_Chains
Python class for discrete Markov chains.  Includes a few common Markov chains.

## Examples
### User-defined Markov chain
```ipython3
In [1]: import Discrete_Markov_Chains as dmc

In [2]: P = {}

In [3]: P['A'] = dmc.dsp.dsp({'B' : 2/3, 'C' : 1/3})

In [4]: P['B'] = dmc.dsp.dsp({'C' : 2/3, 'A' : 1/3})

In [5]: P['C'] = dmc.dsp.dsp({'A' : 2/3, 'B' : 1/3})

In [6]: MC = dmc.dmc(P)

In [7]: walk = dmc.mcwalk(MC, 'A')

In [8]: walk.walk(19)

In [9]: walk
Out[9]: 
A
C
A
C
A
C
A
B
C
A
B
C
B
C
A
B
C
B
C
A

In [10]: walk.sample_dist()
Out[10]: 
C : 0.4
A : 0.35
B : 0.25
```

### Bitstring chain
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
```

### Simple Symmetric Random Walk
```ipython3
In [1]: import Discrete_Markov_Chains as dmc

In [2]: MC = dmc.simple_symm_random_walk()

In [3]: walk = dmc.mcwalk(MC, 0)

In [4]: walk.walk(20)

In [5]: walk
Out[5]: 
0
1
2
3
2
1
2
1
2
3
2
1
0
-1
-2
-3
-4
-3
-2
-1
0
```

### Sliding Puzzle
```ipython3
In [1]: import Discrete_Markov_Chains as dmc

In [2]: MC = dmc.sliding_puzzle(3,3)

In [3]: a = dmc.sliding_puzzle_standard_start(3,3)

In [4]: a
Out[4]: 
[[0 1 2]
 [3 4 5]
 [6 7 8]]

In [5]: walk = dmc.mcwalk(MC, a)

In [6]: walk.walk(9)

In [7]: walk
Out[7]: 
[[0 1 2]
 [3 4 5]
 [6 7 8]]
[[1 0 2]
 [3 4 5]
 [6 7 8]]
[[1 4 2]
 [3 0 5]
 [6 7 8]]
[[1 4 2]
 [0 3 5]
 [6 7 8]]
[[1 4 2]
 [6 3 5]
 [0 7 8]]
[[1 4 2]
 [0 3 5]
 [6 7 8]]
[[1 4 2]
 [3 0 5]
 [6 7 8]]
[[1 0 2]
 [3 4 5]
 [6 7 8]]
[[1 4 2]
 [3 0 5]
 [6 7 8]]
[[1 4 2]
 [3 5 0]
 [6 7 8]]
 ```
